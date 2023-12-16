import ast
imfrom typing import IO

def is_valid_python_source(source: str | IO[str]) -> bool:
    # rest of your code

def is_valid_python_source(source: str | ReadableBuffer) -> bool:
    try:
        ast.parse(source)
    except SyntaxError:
        return False
    return True