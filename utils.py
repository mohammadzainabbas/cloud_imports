import ast
from typing import IO

def is_valid_python_source(source: str | IO[str]) -> bool:
    try:
        ast.parse(source)
    except SyntaxError:
        return False
    return True
