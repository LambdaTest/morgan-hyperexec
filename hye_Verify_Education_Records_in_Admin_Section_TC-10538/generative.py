import aiohttp
import asyncio
import json
import time
import traceback
from typing import Callable, List, Optional, Dict, Any, TypedDict
from pydantic import BaseModel
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from PIL import Image
import io
import base64
import uuid

class GenerativeLogger:
    """Logger that wraps print and prefixes 'GENERATIVE - ' to all messages."""
    
    @staticmethod
    def log(*args, **kwargs):
        """Log message with GENERATIVE prefix."""
        # Convert all arguments to strings and join them
        message = ' '.join(str(arg) for arg in args)
        print(f"GENERATIVE - {message}", **kwargs)
    
    @staticmethod
    def info(*args, **kwargs):
        """Log info message with GENERATIVE prefix."""
        GenerativeLogger.log(*args, **kwargs)
    
    @staticmethod
    def error(*args, **kwargs):
        """Log error message with GENERATIVE prefix."""
        GenerativeLogger.log(*args, **kwargs)
    
    @staticmethod
    def debug(*args, **kwargs):
        """Log debug message with GENERATIVE prefix."""
        GenerativeLogger.log(*args, **kwargs)

class ActorAssetUpdatePayload(BaseModel):
    request_id: str = ""
    compressed_image: str = ""
    tagged_image: str = ""
    tags_desc: dict = {}
    tags_xpath_map: dict = {}
    element_bounds: dict = {}
    window_titles: List[str] = []
    tracked_window_handles: List[str] = []
    

class ActorPayload(BaseModel):
    request_id: str = ""
    objective: str = ""
    expected_output: str = ""
    platform: str = ""
    
class ToolPayload(BaseModel):
    tool_name: str = ""
    tool_args: list[dict[str, dict]] = []
    
class MockOperationPayload(TypedDict):
    operation_intent: str
    locator: list[str]
    operation_type: str
    value: str
    instruction_id: str
    operation_id: str
    optional_flag: bool
    max_retries: int
    retries_delay: int
    explicit_wait: int
    implicit_wait: int
    frame: str
    user_variables: str
    operation_start: str
    operation_end: str
    instruction_module_id: str
    instruction_module_name: str
    use_v2_mobile_tagging: bool
    hard_assertion: bool
    dialog_action: str
    dismiss_dialog: bool
    is_coordinates_used_for_interaction: bool
    element_coordinates_ratio: list[float]
    element_bounds_ratio: list[float]
    kaneaiMobileTaggingImageLimit: int
    clicks_order_code: str
    selector: dict[str, Any]
    manual_interaction_tag: str
    is_global_variable: bool
    is_global_variable_persist: bool
    global_variable_id: str
    mobile_browser: bool
    wait_for_element_timeout: int
    failure_condition: str
    parent_instruction_id: str
    sub_instruction_obj: str
    
    
    
class GenerativeFlowResponse():
    
    def __init__(self, server_url: str = 'https://kaneai-api.lambdatest.com', request_id: str = "", username: str = "", accesskey: str = ""):
        self.server_url = f"{server_url.rstrip('/')}/actor"
        self.username = username
        self.accesskey = accesskey
        self.headers = {'Content-Type': 'application/json', 'Authorization' : f"Basic {base64.b64encode(f'{self.username}:{self.accesskey}'.encode()).decode()}" }
        GenerativeLogger.info(f"Server URL: {self.server_url}")
        self.request_id = request_id
        
    async def _update_actor(self, payload: ActorAssetUpdatePayload):
        """Update the actor with current page assets."""
        url = f"{self.server_url}/update"
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload.model_dump(), headers=self.headers) as response:
                return await response.json()
    
    async def _start_actor(self, payload: ActorPayload):
        """Start the actor with the given objective."""
        url = f"{self.server_url}/start"
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=payload.model_dump(), headers=self.headers) as response:
                    return await response.json()
        except Exception as e:
            GenerativeLogger.error("Error starting actor", e)
            return None
    
    async def _get_tools(self) -> List[ToolPayload]:
        """Get available tools for the current request."""
        url = f"{self.server_url}/tool/{self.request_id}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=self.headers) as response:
                response_data = await response.json()
                return [ToolPayload(**resp) for resp in response_data]
    
    async def _complete_tool(self, payload: ToolPayload):
        """Complete a tool execution."""
        url = f"{self.server_url}/tool/{self.request_id}/complete"
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload.model_dump(), headers=self.headers) as response:
                return await response.json()
    
    async def _wait_for_tools_with_backoff(self, max_attempts: int = 10, base_delay: float = 1, max_delay: float = 5.0) -> List[ToolPayload]:
        """
        Wait for tool responses using exponential backoff.
        
        Args:
            max_attempts: Maximum number of attempts to try
            base_delay: Initial delay in seconds
            max_delay: Maximum delay cap in seconds
            
        Returns:
            List of tool responses, or empty list if none received
        """
        total_wait_time = 0
        
        for attempt in range(max_attempts):
            delay = min(base_delay * (2 ** attempt), max_delay)
            
            await asyncio.sleep(delay)
            total_wait_time += delay
            
            tool_responses = await self._get_tools()
            
            if tool_responses:
                GenerativeLogger.info(f"Tool responses received on attempt {attempt + 1} after {total_wait_time:.1f}s: {tool_responses}")
                return tool_responses
            else:
                GenerativeLogger.info(f"Attempt {attempt + 1}/{max_attempts}: No tool responses after {delay:.1f}s delay, trying again...")
        
        GenerativeLogger.info(f"No tool responses after {max_attempts} attempts (total {total_wait_time:.1f}s)")
        return []


class GenerativeFlow(GenerativeFlowResponse):
    """Web automation and actor communication functionality."""
    
    def __init__(self, server_url: str = "https://kaneai-api.lambdatest.com", driver: WebDriver = None, request_id: str = "xxxxxxxxxxx", platform: str = "web", username: str = "", accesskey: str = ""):
        """Initialize the GenerativeFlow with server configuration."""
        super().__init__(server_url=server_url, request_id=request_id, username=username, accesskey=accesskey)
        self.request_id = request_id
        self.driver: WebDriver = driver
        self.is_running = False
        self.platform = platform
        self.actor_completed = asyncio.Event()
        self.actor_task = None
        self.lambda_executor = None
        self.ui_auction_executor = None
    def set_lambda_executor(self, lambda_executor: Callable):
        self.lambda_executor = lambda_executor
        
    def set_ui_auction_executor(self, ui_auction_executor: Callable):
        self.ui_auction_executor = ui_auction_executor
    
    def set_operations_meta_data_executor(self, operations_meta_data: Callable):
        self.operations_meta_data_executor = operations_meta_data
        
    async def take_screenshot(self, tagify: bool = False) -> str:
        """Take a screenshot of the current page."""
        if not self.driver:
            raise RuntimeError("Driver not initialized. Call create_driver() first.")
            
        if tagify:
            await self.tagify_webpage()
            
        screenshot = self.driver.get_screenshot_as_base64()
        
        if tagify:
            await self.untagify_webpage()
            
        return screenshot
    
    async def tagify_webpage(self, skip_text: bool = True, skip_scroll: bool = True, full_page_tagify: bool = False):
        """Tagify the current webpage for element identification."""
        if not self.driver:
            raise RuntimeError("Driver not initialized. Call create_driver() first.")
            
        try:
            self.driver.execute_script(f"await tagifyWebpage(true, true, {'true' if full_page_tagify else 'false'})")
        except Exception as e:
            GenerativeLogger.error(f"Failed to tagify webpage: {e}")
    
    async def untagify_webpage(self):
        """Remove tags from the webpage."""
        if not self.driver:
            raise RuntimeError("Driver not initialized. Call create_driver() first.")
            
        self.driver.execute_script("await removeLTTags();")
        await asyncio.sleep(0.5)
    
    async def fetch_page_data(self) -> Dict[str, Any]:
        """Fetch all JSON data from the current page."""
        if not self.driver:
            raise RuntimeError("Driver not initialized. Call create_driver() first.")
            
        try:
            url = f"{self.driver.command_executor._url}/session/{self.driver.session_id}/execute/sync"
            response = await self._perform_request(
                url=url, 
                headers={'Content-Type': 'application/json;charset=utf-8'}, 
                payload={"script": 'return fetchAllJsonData()', "args": []}
            )
            parsed_value = response["value"]
            return json.loads(parsed_value)
        except Exception as e:
            GenerativeLogger.error(f"Failed to fetch page data: {e}")
            return {}
    
    async def compress_image(self, image_data: str) -> Optional[str]:
        """Compress a base64 encoded image."""
        try:
            image_bytes = base64.b64decode(image_data)
            with Image.open(io.BytesIO(image_bytes)) as img:
                original_size = len(image_bytes)
                
                if img.width > 1920 or img.height > 1080:
                    max_width, max_height = 1920, 1080
                    ratio = min(max_width/img.width, max_height/img.height)
                    new_width = int(img.width * ratio)
                    new_height = int(img.height * ratio)
                    img = img.resize((new_width, new_height), Image.Resampling.NEAREST)
                
                if img.mode == 'RGBA':
                    img = img.convert('RGB')
                    
                buffer = io.BytesIO()
                img.save(buffer, format="JPEG", optimize=False, quality=80)
                buffer.seek(0)
                compressed_image_data = base64.b64encode(buffer.getvalue()).decode("utf-8")
                
                compressed_size = len(buffer.getvalue())
                if compressed_size < original_size:
                    GenerativeLogger.info("Image compression successful")
                else:
                    GenerativeLogger.info("Image compression did not reduce size")
                    
                return compressed_image_data
        except Exception as e:
            GenerativeLogger.error(f"Error compressing image: {e}")
            return None
    
    async def scrape_page_data(self) -> tuple[str, str, Dict[str, Any]]:
        """Scrape all data from the current page including screenshots and element data."""
        if not self.driver:
            raise RuntimeError("Driver not initialized. Call create_driver() first.")
            
        screenshot = await self.take_screenshot()
        
        await self.tagify_webpage(skip_text=True, skip_scroll=True, full_page_tagify=True)
        await asyncio.sleep(0.5)
        
        json_data = await self.fetch_page_data()
        
        tagged_screenshot = await self.take_screenshot()
        await asyncio.sleep(0.5)
        
        await self.untagify_webpage()
        
        return screenshot, tagged_screenshot, json_data
    
    async def update_actor_assets(self, objective: str, expected_output: str):
        """Update the actor with current page assets."""
        screenshot, tagged_screenshot, json_data = await self.scrape_page_data()
        
        compressed_screenshot = await self.compress_image(screenshot)
        compressed_tagged_screenshot = await self.compress_image(tagged_screenshot)
        
        update_payload = ActorAssetUpdatePayload(
            request_id=self.request_id,
            compressed_image=compressed_screenshot or "",
            tagged_image=compressed_tagged_screenshot or "",
            tags_xpath_map=json_data.get("JSONOutput", {}),
            element_bounds=json_data.get("elementRectOutput", {}),
            tags_desc=json_data.get("descOutput", {}),
            window_titles=[],
            tracked_window_handles=[],
            platform=self.platform
        )
        
        await self._update_actor(update_payload)
    
    async def _start_actor_detached(self, objective: str, expected_output: str):
        """Internal method to start the actor in a detached thread."""
        try:
            start_payload = ActorPayload(
                request_id=self.request_id,
                objective=objective,
                expected_output=expected_output,
                platform=self.platform
            )
            
            response = await self._start_actor(start_payload)
            
            if response:
                GenerativeLogger.info(f"Actor completed successfully:")
                self.actor_completed.set()
            else:
                GenerativeLogger.error("Actor failed to start or returned no response")
                self.actor_completed.set()
                
        except Exception as e:
            GenerativeLogger.error(f"Error in detached actor thread: {e}")
            traceback.print_exc()
            self.actor_completed.set()
    
    def start_actor(self, objective: str, expected_output: str):
        """Start the actor with the given objective in a detached thread."""
        self.actor_completed.clear()
        
        self.actor_task = asyncio.create_task(
            self._start_actor_detached(objective, expected_output)
        )
        
        GenerativeLogger.info("Actor started in detached thread")
    
    def is_actor_completed(self) -> bool:
        """Check if the actor has completed its job."""
        return self.actor_completed.is_set()
    
    async def wait_for_actor_completion(self, timeout: float = None) -> bool:
        """Wait for the actor to complete its job."""
        try:
            await asyncio.wait_for(self.actor_completed.wait(), timeout=timeout)
            return True
        except asyncio.TimeoutError:
            return False
    
    async def run_automation_loop(self, objective: str, expected_output: str, url: str = None):
        """Main automation loop that handles the complete workflow."""
        try:
            if not self.driver:
                raise RuntimeError("Driver not provided. Please pass a driver in the constructor.")
            
            if url:
                self.driver.get(url=url)
            
            await self.update_actor_assets(objective, expected_output)
            
            self.start_actor(objective, expected_output)
            
            self.is_running = True
            
            while self.is_running:
                try:
                    if self.is_actor_completed():
                        GenerativeLogger.info("Actor has completed its job, breaking automation loop...")
                        break
                    
                    try:
                        tool_responses = await asyncio.wait_for(
                            self._wait_for_tools_with_backoff(), 
                            timeout=10.0
                        )
                    except asyncio.TimeoutError:
                        continue
                    
                    if not tool_responses:
                        GenerativeLogger.info("No tool responses received, continuing to wait...")
                        continue
                        
                    GenerativeLogger.debug(f"Processing tool responses: {tool_responses}")
                    tool = tool_responses[0]
                    tool_args = tool.tool_args[0]
                    operations_meta_data:MockOperationPayload={
                        "operation_intent": tool_args.get("operation", {}).get("operation", ""),
                        "locator": [tool_args.get("execution_args", {}).get("xpath", "")],
                        "operation_type": tool_args.get("operation", {}).get("operation_dict", {}).get("operation_type", ""),
                        "value": tool_args.get("operation", {}).get("operation_dict", {}).get("value", ""),
                        "instruction_id": str(uuid.uuid4()),
                        "operation_id": str(uuid.uuid4()),
                        "optional_flag": False,
                        "max_retries": 0,
                        "retries_delay": 0,
                        "explicit_wait": 0,
                        "implicit_wait": 0,
                        "frame": "",
                        "user_variables": "",
                        "operation_start": None,
                        "operation_end": None,
                        "instruction_module_id": "",
                        "instruction_module_name": "",
                        "use_v2_mobile_tagging": False,
                        "hard_assertion": False,
                        "dialog_action": "",
                        "dismiss_dialog": False,
                        "is_coordinates_used_for_interaction": False,
                        "element_coordinates_ratio": [],
                        "element_bounds_ratio": [],
                        "kaneaiMobileTaggingImageLimit": 1,
                        "clicks_order_code": "se_js_ac",
                        "selector": {},
                        "manual_interaction_tag": "",
                        "is_global_variable": False,
                        "is_global_variable_persist": False,
                        "global_variable_id": "",
                        "mobile_browser": False,
                        "wait_for_element_timeout": 0,
                        "failure_condition": "",
                        "parent_instruction_id": "",
                        "sub_instruction_obj": json.dumps(tool_args.get("operation", {})),
                        "unresolved": False
                    }
                    self.operations_meta_data_executor({"0":operations_meta_data})
                    self.ui_auction_executor(self.driver, 0)
                    
                    await self.update_actor_assets(objective, expected_output)
                    
                    for tool_response in tool_responses:
                        await self._complete_tool(tool_response)
                    
                except KeyboardInterrupt:
                    GenerativeLogger.info("Keyboard interrupt received")
                    break
                    
        except Exception as e:
            GenerativeLogger.error(f"Error in automation loop: {e}")
            traceback.print_exc()
        finally:
            await self.cleanup()
    
    async def cleanup(self):
        """Clean up resources."""
        self.is_running = False
        
        if self.actor_task and not self.actor_task.done():
            GenerativeLogger.info("Cancelling actor task...")
            self.actor_task.cancel()
            try:
                await self.actor_task
            except asyncio.CancelledError:
                GenerativeLogger.info("Actor task cancelled successfully")
            except Exception as e:
                GenerativeLogger.error(f"Error cancelling actor task: {e}")
    
    async def _perform_request(self, url: str, headers: Dict = None, payload: Dict = None, 
                             method: str = "post", params: Dict = None, timeout: int = 180):
        """Perform HTTP request."""
        timeout_obj = aiohttp.ClientTimeout(total=timeout)
        
        async with aiohttp.ClientSession(timeout=timeout_obj) as session:
            request_kwargs = {
                "headers": headers,
                "params": params
            }
            
            if payload is not None:
                if isinstance(payload, dict):
                    request_kwargs["json"] = payload
                else:
                    request_kwargs["data"] = payload
            
            async with session.request(method.lower(), url, **request_kwargs) as response:
                return await response.json()