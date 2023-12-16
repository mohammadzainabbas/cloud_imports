import ast
from typing import IO

def is_valid_python_code(code: str | IO[str]) -> bool:
    """
    Check if the given code is valid Python code.
    """
    try:
        ast.parse(code)
    except SyntaxError:
        return False
    return True
