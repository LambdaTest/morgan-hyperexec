import colorsys
import random
import aiohttp
import asyncio
import json
import time
import traceback
from typing import Callable, List, Optional, Dict, Any, TypedDict
from pydantic import BaseModel
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from PIL import Image, ImageDraw, ImageFont
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
    platform: str = ""

    # specific for mobile
    page_source: Optional[str] = ""
    is_mobile: Optional[bool] = False
    is_mobile_browser: Optional[bool] = False
    device_os: Optional[str] = ""
    untagged_image_base64: Optional[str] = ""
    driver_window_size: dict = {}
    

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
    
    def __init__(self, server_url: str = "https://kaneai-api.lambdatest.com", driver: WebDriver = None, request_id: str = "xxxxxxxxxxx", platform: str = "web", username: str = "", accesskey: str = "", mobile_tagify_script: str = ""):
        """Initialize the GenerativeFlow with server configuration."""
        super().__init__(server_url=server_url, request_id=request_id, username=username, accesskey=accesskey)
        self.request_id = request_id
        self.driver: WebDriver = driver
        self.is_running = False
        self.platform = platform
        self.actor_completed = asyncio.Event()
        self.actor_task = None
        self.lambda_executor = None
        self.ui_action_executor = None
        self.mobile_tagify_script = mobile_tagify_script


    def set_lambda_executor(self, lambda_executor: Callable):
        self.lambda_executor = lambda_executor
        
    def set_ui_action_executor(self, ui_action_executor: Callable):
        self.ui_action_executor = ui_action_executor
    
    def set_operations_meta_data_executor(self, operations_meta_data: Callable):
        self.operations_meta_data_executor = operations_meta_data


    def is_mobile_test(self) -> bool:
        """Check if the test is a mobile test."""
        return self.driver.capabilities.get('platformName', 'android').lower() in ["android", "ios"]

    def is_mobile_app_test(self) -> bool:
        """Check if the test is a mobile test."""
        return self.platform.lower() == "mobile"

    def is_mobile_browser_test(self) -> bool:
        """Check if the test is a mobile browser test."""
        return self.is_mobile_test() and not self.is_mobile_app_test()

    def get_device_os(self) -> str:
        """Get the device OS."""
        return str(self.driver.capabilities.get('platformName', 'android')).lower()

        
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
                
                if img.mode != 'RGB':
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

    async def tagify_mobile_browser_webpage(self, skip_text=True, skip_scroll=True, full_page_tagify=True) -> tuple[str, Dict[str, Any]]:
        """Tagify the current mobile browser webpage for element identification."""
        if not self.mobile_tagify_script:
            raise RuntimeError("Mobile tagify script not initialized.")

        tagify_response = {}
        tagified_image = ""
        try:        
            self.driver.execute_script(self.mobile_tagify_script)
            skip_text = 'true' if skip_text else 'false'
            skip_scroll = 'true' if skip_scroll else 'false'
            full_page_tagify = 'true' if full_page_tagify else 'false'
            tagify_response = self.driver.execute_script(f"return tagifyWebpage({skip_text}, {skip_scroll}, {full_page_tagify});")
            tagified_image, ratio = self.make_tagged_screenshot(screenshot_base64=self.driver.get_screenshot_as_base64(),rects=tagify_response.get("rects", {}), driver=self.driver)
            
            # add keys to match web output
            tagify_response["JSONOutput"] = tagify_response.get("xpaths", {})
            tagify_response["descOutput"] = tagify_response.get("descriptions", {})
            tagify_response["elementRectOutput"] = tagify_response.get("rects", {})
            return tagified_image, tagify_response
        except Exception as e:
            GenerativeLogger.error(f"Failed to tagify webpage: {e}")
            return tagified_image, tagify_response
    

    
    async def scrape_page_data(self) -> tuple[str, str, Dict[str, Any]]:
        """Scrape all data from the current page including screenshots and element data."""
        if not self.driver:
            raise RuntimeError("Driver not initialized. Call create_driver() first.")
            
        screenshot = await self.take_screenshot()

        if self.is_mobile_app_test():
            return screenshot, "", {}
        
        # for web tagification
        skip_text=True
        skip_scroll=True
        full_page_tagify=True

        if self.is_mobile_browser_test():
            tagified_image, tagify_response = await self.tagify_mobile_browser_webpage(skip_text=skip_text, skip_scroll=skip_scroll, full_page_tagify=full_page_tagify)
            return screenshot, tagified_image, tagify_response

        await self.tagify_webpage(skip_text=skip_text, skip_scroll=skip_scroll, full_page_tagify=full_page_tagify)
        await asyncio.sleep(0.5)
        
        json_data = await self.fetch_page_data()
        
        tagged_screenshot = await self.take_screenshot()
        await asyncio.sleep(0.5)
        
        await self.untagify_webpage()
        
        return screenshot, tagged_screenshot, json_data
    
    async def update_actor_assets(self, objective: str, expected_output: str):
        """Update the actor with current page assets."""
        screenshot, tagged_screenshot, json_data = await self.scrape_page_data()
        
        if not self.is_mobile_app_test():
            compressed_screenshot = await self.compress_image(screenshot)
        else:
            compressed_screenshot = ""

        compressed_tagged_screenshot = ""
        if tagged_screenshot:
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
            platform=self.platform,
            page_source=self.driver.page_source.replace('\r\n', ''),
            is_mobile=self.is_mobile_test(),
            is_mobile_browser=self.is_mobile_browser_test(),
            device_os=self.get_device_os(),
            untagged_image_base64=screenshot if self.is_mobile_app_test() else "",
            driver_window_size=self.driver.get_window_size(),
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
                            timeout=30.0
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
                        "is_coordinates_used_for_interaction": tool_args.get("execution_args", {}).get("is_coordinates_used_for_interaction", False),
                        "element_coordinates_ratio": tool_args.get("execution_args", {}).get("element_coordinates_ratio", []),
                        "element_bounds_ratio": tool_args.get("execution_args", {}).get("element_bounds_ratio", []),
                        "kaneaiMobileTaggingImageLimit": 1,
                        "clicks_order_code": "se_js_ac",
                        "selector": {},
                        "manual_interaction_tag": "",
                        "is_global_variable": False,
                        "is_global_variable_persist": False,
                        "global_variable_id": "",
                        "mobile_browser": self.is_mobile_browser_test(),
                        "wait_for_element_timeout": 0,
                        "failure_condition": "",
                        "parent_instruction_id": "",
                        "sub_instruction_obj": json.dumps(tool_args.get("operation", {})),
                        "unresolved": False
                    }
                    self.operations_meta_data_executor({"0":operations_meta_data})
                    self.ui_action_executor(self.driver, 0)
                    
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



    def make_tagged_screenshot(self, screenshot_base64, rects, driver):
            """
            Draw colored borders around rectangles and add labeled squares
            
            Args:
                screenshot_base64: Screenshot image as base64-encoded string
                rects: Dictionary with keys and rect coordinates {'key': {'left': x, 'top': y, 'width': w, 'height': h}}
                output_path: Path to save the annotated image (optional)
                border_width: Width of the border lines
            
            Returns:
                Path to the annotated image
            """
            def generate_random_color():
                """Generate a random bright color"""
                # Generate random hue, with high saturation and value for bright colors
                hue = random.random()
                saturation = random.uniform(0.7, 1.0)
                value = random.uniform(0.8, 1.0)
                    
                # Convert HSV to RGB
                rgb = colorsys.hsv_to_rgb(hue, saturation, value)
                return tuple(int(c * 255) for c in rgb)

            def are_rectangles_disjoint(r1, r2):

                def is_inside(inner, outer):
                    return (inner[0] >= outer[0] and inner[1] >= outer[1] and inner[2] <= outer[2] and inner[3] <= outer[3])

                if is_inside(r1, r2) or is_inside(r2, r1):
                    return False

                if not (r1[2] <= r2[0] or r1[0] >= r2[2] or r1[3] <= r2[1] or r1[1] >= r2[3]):   
                    return False
                return True
            
            try:
                # Decode base64 screenshot
                image_data = base64.b64decode(screenshot_base64)
                image = Image.open(io.BytesIO(image_data))
                original_image = image.copy()
                draw = [ImageDraw.Draw(image)]
                ratio = driver.execute_script("return window.devicePixelRatio;")
                for key, rect in rects.items():
                    if rect['x'] * ratio > image.width and rect['x'] <= image.width:
                        ratio = 1

                status_bar_height = 0
                if self.get_device_os() == 'ios':
                    try:
                        # to subtract the status bar height in ios
                        status_bar_height = driver.execute_script("mobile: deviceScreenInfo").get('statusBarSize',0).get('height', 0)
                    except Exception as e:
                        status_bar_height = 0

                # Font paths
                font_paths = [
                    "serif.ttf"
                ]

                # Process each rectangle
                tagifified_images = [image]
                image_to_rect_mapping = [[]]
                max_image_num = 1
                for key, rect in rects.items():
                    color = generate_random_color()
                    left, top, width, height = rect['x'] * ratio , ((rect['top'] + status_bar_height) * ratio), rect['width'] * ratio, rect['height'] * ratio
                    x1, y1 = int(left), int(top)
                    x2, y2 = int(left + width), int(top + height)

                    image_num = 0
                    for index in range(0, max_image_num):
                        if index >= len(image_to_rect_mapping):
                            image_to_rect_mapping.append([])
                        rects = image_to_rect_mapping[index]
                        is_space_available = True
                        for rect in rects:
                            if not are_rectangles_disjoint([x1, y1, x2, y2], [rect['x1'], rect['y1'], rect['x2'], rect['y2']]):
                                is_space_available = False
                                break

                        if is_space_available or index+1 == max_image_num:
                            image_num = index
                            image_to_rect_mapping[image_num].append({'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2})
                            break
                    if image_num >= len(tagifified_images):
                        tagifified_images.append(original_image.copy())
                        draw.append(ImageDraw.Draw(tagifified_images[image_num]))

                    for i in range(3):
                        draw[image_num].rectangle([x1-i, y1-i, x2+i, y2+i], outline=color, fill=None)

                    square_width = min(40, width // 2)
                    square_height = min(40, height // 2)

                    draw[image_num].rectangle([x2-square_width, y2-square_height, x2, y2], outline=color, fill=color)

                    text_color = (255, 255, 255) if sum(color) < 382 else (0, 0, 0)  # White text for dark bg, black for light bg

                    for font_path in font_paths:
                        try:
                            draw[image_num].text(
                                xy=(x2 - square_width + 3, y2 - square_height + 3),
                                text=key,
                                fill= text_color,
                                font=ImageFont.truetype(font_path, max( 1, min(square_height, square_width) - 5))
                            )
                            break
                        except IOError:
                            continue

                with io.BytesIO() as buffer:
                    if tagifified_images[0].mode != 'RGB':
                        tagifified_images[0] = tagifified_images[0].convert('RGB')
                    tagifified_images[0].save(buffer, format="JPEG", optimize=True, quality=50)
                    return base64.b64encode(buffer.getvalue()).decode('utf-8') , ratio

            except Exception as e:
                print(f"✗ Error creating annotated image: {e}")
                return None