
# define orangehrm_login_module_1_0 module
from UIActions import ui_action, lambda_hooks, vision_query, perform_assertion, string_to_float, user_variables, access_value
try:
   from UIActions import driver_query_script
except ImportError:
   pass
import UIActions

def orangehrm_login_module_1_0(driver):
        # navigate to 'https://orange-hrm.lambdatestinternal.com/orangehrm-5.7' website
        lambda_hooks(driver, f"open url {UIActions.operations_meta_data['0']['url']}")
        ui_action(driver = driver, operation_index = str(0))

        # Query 'Username input box' visibility
        lambda_hooks(driver, "Query 'Username input box' visibility")
        Username_input_box_visible = vision_query(driver = driver, operation_index = str(1))
        if isinstance(Username_input_box_visible, dict):
            Username_input_box_visible = Username_input_box_visible.get("vision_query")
        user_variables["Username_input_box_visible"] =  Username_input_box_visible
        print("Username_input_box_visible:", Username_input_box_visible)

        # set the value of variable 'assertion_operand_556c32c0518b47e58d564f2859a0e0cb_0' to true
        lambda_hooks(driver, "set the value of variable 'assertion_operand_556c32c0518b47e58d564f2859a0e0cb_0' to true")
        assertion_operand_556c32c0518b47e58d564f2859a0e0cb_0 = "true"
        ui_action(driver = driver, operation_index = str(2))
        assertion_result = ui_action(driver=driver, operation_index=str(3))
        print("assertion_result: ", assertion_result)

        # type 'pushpa.raj' in Username
        lambda_hooks(driver, f"type {UIActions.operations_meta_data['4']['value']}")
        ui_action(driver = driver, operation_index = str(4))

        # type ******************* in Password input field
        lambda_hooks(driver, f"type {UIActions.operations_meta_data['5']['value']}")
        ui_action(driver = driver, operation_index = str(5))

        # Click 'Login'
        lambda_hooks(driver, "Click 'Login'")
        ui_action(driver = driver, operation_index = str(6))
