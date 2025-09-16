from __future__ import annotations
import enum
from enum import Enum
from typing import Union, List, Any, Optional
from functools import reduce
import operator as _op
from typing import Callable


class ResolvedCondition:
    def __init__(self, left_operand: str, operator: PossibleCondition, right_operand: str):
        self.left_operand = left_operand
        self.operator = operator
        self.right_operand = right_operand
        
    
    def to_dict(self):
        return {
            "left_operand": self.left_operand,
            "operator": self.operator.value,
            "right_operand": self.right_operand,
        }
    
    @classmethod
    def from_string(cls, condition: str):
        # split the condition into left_operand, operator, right_operand
        # if the condition is not a string, return the condition
        left_operand, _operator, right_operand = condition.split()
        operator = PossibleCondition(_operator.strip())
        return cls(left_operand.strip(), operator, right_operand.strip())
    
    
    @classmethod
    def from_json(cls, json_data):
        return cls(
            left_operand = json_data.get('left_operand', ''),
            operator = PossibleCondition(json_data.get('operator', '')),
            right_operand = json_data.get('right_operand', ''),
        )
        
    @classmethod
    def create_string_from_condition(cls, conditions: list[ResolvedCondition], connectors: list[ConcatenationOperator]):
        condition_string = ""
        for idx, condition in enumerate(conditions):
            condition_string += str(condition)
            if idx < len(connectors):
                condition_string += connectors[idx].value
        return condition_string
    
    
    def __str__(self):
        return f"{self.left_operand} {self.operator.value} {self.right_operand}"
    
    def __eq__(self, other):
        if not isinstance(other, ResolvedCondition):
            return False
        return self.left_operand == other.left_operand and self.operator == other.operator and self.right_operand == other.right_operand
        
class PossibleCondition(enum.Enum):
    EQUALS = "=="
    NOT_EQUALS = "!="
    GREATER_THAN = ">"
    LESS_THAN = "<"
    GREATER_THAN_OR_EQUALS = ">="
    LESS_THAN_OR_EQUALS = "<="
    CONTAINS = "contains"
    NOT_CONTAINS = "not_contains"
    STARTS_WITH = "starts_with"
    ENDS_WITH = "ends_with"
    # add default value for all the operators
    
    @classmethod
    def _missing_(cls, value):
        # incase of invalid operator, return the default value
        return cls.EQUALS
    
    def __str__(self):
        return self.value
    
    def __eq__(self, other):
        if not isinstance(other, PossibleCondition):
            return False
        return self.value == other.value
    


class MathOperationOperator(enum.Enum):
    #add|subtract|multiply|divide|mod|pow|negate|abs
    ADD = "add"
    SUBTRACT = "subtract"
    MULTIPLY = "multiply"
    DIVIDE = "divide"
    MODULUS = "mod"
    POWER = "pow"
    NEGATE = "negate"
    ABS = "abs"
        
    

class Mathmatic:
    def __init__(self, operator: MathOperationOperator, operands: list[Union[str, Mathmatic]]): # operator can be int (in form of string) or placeholder {{}} / ${} in form of string or MathOperation object
        self.operator = operator
        self.operands = operands
        # add validation check if operator is subtract or divide, then the length of operands should be 2
        if self.operator in [MathOperationOperator.SUBTRACT, MathOperationOperator.DIVIDE, MathOperationOperator.MODULUS]:
            if len(self.operands) != 2:
                raise ValueError("Subtract and Divide operators require exactly 2 operands")
        # add validation check if operator is negate, then the length of operands should be 1
        if self.operator == MathOperationOperator.NEGATE:
            if len(self.operands) != 1:
                raise ValueError("Negate operator require exactly 1 operand")
        # add validation check if operator is abs, then the length of operands should be 1
        if self.operator == MathOperationOperator.ABS:
            if len(self.operands) != 1:
                raise ValueError("Abs operator require exactly 1 operand")
        
    
    def to_dict(self):
        return {
            "operator": self.operator.value,
            "operands": [operand.to_dict() if isinstance(operand, Mathmatic) else operand for operand in self.operands],
        }
    


    def _resolve_placeholder(self, s: str, variables: dict, get_variable_value: Callable, *args, **kwargs):
        if get_variable_value is not None and isinstance(get_variable_value, Callable):
            return get_variable_value(s, variables, *args, **kwargs)
        s = s.strip()
        if s.startswith("{{") and s.endswith("}}"):
            key = s[2:-2].strip()
            try:
                return self._access_nested_value(variables, key)
            except (KeyError, TypeError, IndexError) as e:
                raise KeyError(f"Variable '{key}' not found in variables: {e}")
        if s.startswith("${") and s.endswith("}"):
            key = s[2:-1].strip()
            try:
                return self._access_nested_value(variables, key)
            except (KeyError, TypeError, IndexError) as e:
                raise KeyError(f"Variable '{key}' not found in variables: {e}")
        return s  # not a placeholder

    def _access_nested_value(self, variable_dump, name):
        """
        Access nested values in a dictionary using dot notation.
        Handles keys like 'api_variablebe40.response_body.amount'
        """
        keys = name.split('.')
        value = variable_dump

        for key in keys:
            while '[' in key and ']' in key:
                # Handle nested list indexing
                base_key, index = key.split('[', 1)
                index = int(index.split(']')[0])
                value = value[base_key] if base_key else value
                value = value[index]
                key = key[key.index(']') + 1:]  # Move to the next part of the key

            if key:  # Handle any remaining dictionary key
                value = value[key]
        return value

    def _as_number(self, value):
        # Convert value to float if possible; raise if not numeric
        if isinstance(value, (int, float)):
            return float(value)
        if isinstance(value, str):
            # Try to parse numeric string
            try:
                return float(value.strip())
            except ValueError:
                raise ValueError(f"Non-numeric operand encountered: {value!r}")
        raise ValueError(f"Unsupported operand type: {type(value).__name__}")

    def evaluate(self, variables: dict, get_variable_value: Callable, *args, **kwargs):
        # Resolve all operands to numbers (recursively for nested operations, and resolving placeholders)
        resolved = []
        for operand in self.operands:
            if isinstance(operand, Mathmatic):
                resolved.append(self._as_number(operand.evaluate(variables, get_variable_value, *args, **kwargs)))
            else:
                # Resolve placeholders if it's a string
                if isinstance(operand, str):
                    operand = self._resolve_placeholder(operand, variables, get_variable_value, *args, **kwargs)
                resolved.append(self._as_number(operand))

        if self.operator == MathOperationOperator.ADD:
            return sum(resolved)
        elif self.operator == MathOperationOperator.SUBTRACT:
            return resolved[0] - resolved[1]
        elif self.operator == MathOperationOperator.MULTIPLY:
            return reduce(_op.mul, resolved, 1.0)
        elif self.operator == MathOperationOperator.DIVIDE:
            if resolved[1] == 0:
                raise ZeroDivisionError("Division by zero")
            return resolved[0] / resolved[1]
        elif self.operator == MathOperationOperator.MODULUS:
            if resolved[1] == 0:
                raise ZeroDivisionError("Modulo by zero")
            return resolved[0] % resolved[1]
        elif self.operator == MathOperationOperator.POWER:
            return resolved[0] ** resolved[1]
        elif self.operator == MathOperationOperator.NEGATE:
            return -resolved[0]
        elif self.operator == MathOperationOperator.ABS:
            return abs(resolved[0])
        else:
            raise ValueError(f"Unsupported operator: {self.operator}")
    
    
    @classmethod
    def from_json(cls, json_data):
        """
        Create a MathOperation from JSON data.
        Handles nested operations by recursively creating MathOperation objects.
        """
        operator = MathOperationOperator(json_data.get('operator', 'add')) 
        operands = []
        
        for operand in json_data.get('operands', []):
            if isinstance(operand, dict) and 'operator' in operand:
                # This is a nested MathOperation
                operands.append(cls.from_json(operand))
            else:
                # This is a simple operand (string, number, etc.)
                operands.append(operand)
        
        return cls(operator=operator, operands=operands)
    
    
    

class AssertionCondition(enum.Enum):
    #"equals|not_equals|greater_than|less_than|greater_than_or_equal|less_than_or_equal|starts_with|ends_with|contains|length_equals|type_equals|json_key_exists|json_keys_count|json_array_length_equals|json_array_contains|json_value_equals",
    EQUALS = "equals"
    NOT_EQUALS = "not_equals"
    GREATER_THAN = "greater_than"
    LESS_THAN = "less_than"
    GREATER_THAN_OR_EQUALS = "greater_than_or_equal"
    LESS_THAN_OR_EQUALS = "less_than_or_equal"
    STARTS_WITH = "start_with"
    ENDS_WITH = "end_with"
    CONTAINS = "contains"
    NOT_CONTAINS = "not_contains"
    LENGTH_EQUALS = "length_equals"
    TYPE_EQUALS = "type_equals"
    JSON_KEY_EXISTS = "json_key_exists"
    JSON_KEYS_COUNT = "json_keys_count"
    JSON_ARRAY_LENGTH_EQUALS = "json_array_length_equals"
    JSON_ARRAY_CONTAINS = "json_array_contains"
    JSON_VALUE_EQUALS = "json_value_equals"
    # add default value for all the operators
    @classmethod
    def _missing_(cls, value):
        # incase of invalid operator, return the default value
        return cls.EQUALS
    
    def __str__(self):
        return self.value
    
    def __eq__(self, other):
        if not isinstance(other, AssertionCondition):
            return False
        return self.value == other.value
    
class ConcatenationOperator(enum.Enum):
    AND = "AND"
    OR = "OR"


class Assertion:
    def __init__(
        self,
        assertion_operator: Union[AssertionCondition, List[AssertionCondition], ConcatenationOperator] = None,  # leaf: equals, [equals], or group: AND/OR
        assertion_operands: Optional[List[ConcatenationOperator]] = None,   # group: [AND] or [OR] (usually one)
        left_operand: Any = None,
        right_operand: Any = None,
        operands: Optional[List["Assertion"]] = None,                       # children for logical groups
        operator: Union[AssertionCondition, ConcatenationOperator] = None   # alias for assertion_operator for backward compatibility
    ):
        # Handle backward compatibility with 'operator' parameter
        if operator is not None and assertion_operator is None:
            assertion_operator = operator
            
        # Handle single operator vs list of operators
        if isinstance(assertion_operator, AssertionCondition):
            self.assertion_operator = [assertion_operator]
            self.assertion_operands = assertion_operands or []
        elif isinstance(assertion_operator, ConcatenationOperator):
            self.assertion_operator = []
            self.assertion_operands = [assertion_operator]
        elif isinstance(assertion_operator, list):
            self.assertion_operator = assertion_operator
            self.assertion_operands = assertion_operands or []
        else:
            self.assertion_operator = []
            self.assertion_operands = assertion_operands or []
        self.left_operand = left_operand
        self.right_operand = right_operand
        self.operands = operands or []   # if non-empty, this node is a logical group

    # ---------- helpers ----------
    def _resolve(self, value, variables: dict, get_variable_value: Callable, *args, **kwargs):
        if isinstance(value, str):
            if isinstance(get_variable_value, Callable) and get_variable_value is not None:
                s = get_variable_value(value, variables, *args, **kwargs)
                try:
                    return float(s)
                except ValueError:
                    return value
            s = value.strip()
            if s.startswith("{{") and s.endswith("}}"):
                key = s[2:-2].strip()
                return self._access_nested_value(variables, key)
            if s.startswith("${") and s.endswith("}"):
                key = s[2:-1].strip()
                return self._access_nested_value(variables, key)
            # best-effort numeric parse; otherwise leave as string
            try:
                return float(s)
            except ValueError:
                return value
        return value

    def _access_nested_value(self, variable_dump, name):
        """
        Access nested values in a dictionary using dot notation.
        Handles keys like 'api_variablebe40.response_body.amount'
        """
        keys = name.split('.')
        value = variable_dump

        for key in keys:
            while '[' in key and ']' in key:
                # Handle nested list indexing
                base_key, index = key.split('[', 1)
                index = int(index.split(']')[0])
                value = value[base_key] if base_key else value
                value = value[index]
                key = key[key.index(']') + 1:]  # Move to the next part of the key

            if key:  # Handle any remaining dictionary key
                value = value[key]
        return value

    def _eval_leaf_condition(self, cond: AssertionCondition, left, right) -> bool:
        if cond == AssertionCondition.EQUALS:
            return left == right
        if cond == AssertionCondition.NOT_EQUALS:
            return left != right
        if cond == AssertionCondition.GREATER_THAN:
            return left > right
        if cond == AssertionCondition.LESS_THAN:
            return left < right
        if cond == AssertionCondition.GREATER_THAN_OR_EQUALS:
            return left >= right
        if cond == AssertionCondition.LESS_THAN_OR_EQUALS:
            return left <= right
        if cond == AssertionCondition.CONTAINS:
            return str(right) in str(left)
        if cond == AssertionCondition.NOT_CONTAINS:
            return str(right) not in str(left)
        if cond == AssertionCondition.STARTS_WITH:  # note: enum value is "start_with"
            return str(left).startswith(str(right))
        if cond == AssertionCondition.ENDS_WITH:    # enum value is "end_with"
            return str(left).endswith(str(right))
        if cond == AssertionCondition.LENGTH_EQUALS:
            return len(left) == int(right)
        if cond == AssertionCondition.TYPE_EQUALS:
            return type(left).__name__ == str(right)
        if cond == AssertionCondition.JSON_KEY_EXISTS:
            return isinstance(left, dict) and str(right) in left
        if cond == AssertionCondition.JSON_KEYS_COUNT:
            return isinstance(left, dict) and len(left.keys()) == int(right)
        if cond == AssertionCondition.JSON_ARRAY_LENGTH_EQUALS:
            return isinstance(left, list) and len(left) == int(right)
        if cond == AssertionCondition.JSON_ARRAY_CONTAINS:
            return isinstance(left, list) and right in left
        if cond == AssertionCondition.JSON_VALUE_EQUALS:
            # Expect right as [key, value]
            return isinstance(left, dict) and isinstance(right, (list, tuple)) and len(right) == 2 and left.get(str(right[0])) == right[1]
        raise ValueError(f"Unsupported condition: {cond}")

    # ---------- public API ----------
    def evaluate(self, variables: dict, get_variable_value: Callable, *args, **kwargs) -> bool:
        # Logical group node
        if self.operands:
            # If we have operands but no assertion_operands, check if we have a single operator
            if not self.assertion_operands:
                # Check if we have a single operator in assertion_operator (for backward compatibility)
                if len(self.assertion_operator) == 1 and isinstance(self.assertion_operator[0], ConcatenationOperator):
                    op = self.assertion_operator[0]
                else:
                    # Default to AND if no operator specified
                    op = ConcatenationOperator.AND
            else:
                # Use the first operator from assertion_operands
                op = self.assertion_operands[0]

            # fold with the operator between children
            result = self.operands[0].evaluate(variables, get_variable_value, *args, **kwargs)
            for idx in range(1, len(self.operands)):
                val = self.operands[idx].evaluate(variables, get_variable_value, *args, **kwargs)
                if op == ConcatenationOperator.AND:
                    result = result and val
                elif op == ConcatenationOperator.OR:
                    result = result or val
                else:
                    raise ValueError(f"Unsupported logical operator: {op}")
            return result

        # Leaf comparison node: all listed conditions must hold (logical AND)
        left = self._resolve(self.left_operand, variables, get_variable_value, *args, **kwargs)
        right = self._resolve(self.right_operand, variables, get_variable_value, *args, **kwargs)
        for cond in self.assertion_operator:
            if not self._eval_leaf_condition(cond, left, right):
                return False
        return True

    def to_dict(self) -> dict:
        return {
            "operator": [op.value for op in self.assertion_operator],
            "assertion_operands": [op.value for op in self.assertion_operands],
            "left_operand": self.left_operand,
            "right_operand": self.right_operand,
            "operands": [child.to_dict() for child in self.operands] if self.operands else []
        }

    
    @classmethod
    def from_json(cls, json_data: dict) -> "Assertion":
        # Check if this is a logical group by looking at assertion_operands first (new format)
        assertion_operands = json_data.get("assertion_operands", [])
        if assertion_operands and assertion_operands[0] in ConcatenationOperator._value2member_map_:
            # This is a logical group (new format)
            concat = ConcatenationOperator(assertion_operands[0])
            children = [cls.from_json(o) for o in json_data.get("operands", [])]
            return cls(
                assertion_operator=[],
                assertion_operands=[concat],
                operands=children
            )
        
        # Check if this is a logical group by looking at operator field (old format)
        op_data = json_data.get("operator", [])
        if isinstance(op_data, str) and op_data in ConcatenationOperator._value2member_map_:
            # This is a logical group (old format)
            concat = ConcatenationOperator(op_data)
            children = [cls.from_json(o) for o in json_data.get("operands", [])]
            return cls(
                assertion_operator=[],
                assertion_operands=[concat],
                operands=children
            )
        
        # Handle leaf nodes - both single operator string and list of operators
        if isinstance(op_data, list):
            conditions = [AssertionCondition(op) for op in op_data] if op_data else [AssertionCondition.EQUALS]
        else:
            conditions = [AssertionCondition(op_data)] if op_data else [AssertionCondition.EQUALS]
            
        return cls(
            assertion_operator=conditions,
            left_operand=json_data.get("left_operand"),
            right_operand=json_data.get("right_operand")
        )
