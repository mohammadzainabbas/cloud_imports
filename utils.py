import ast
from typing import IO, Optional
from requests import get
from requests.exceptions import HTTPError
from logging import Logger

def is_valid_python_code(code: str | IO[str]) -> bool:
    """
    Check if the given code is valid Python code.
    """
    try:
        ast.parse(code)
    except SyntaxError:
        return False
    return True

def get_remote_python_source(url: str, logger: Optional[Logger] = None) -> str | None:
    """
    Get the Python source code from the given URL.
    """
    try:
        logger.debug(f"Getting remote Python source from {url}")
        response = get(url)
        response.raise_for_status()
        source = response.text
        if not is_valid_python_code(source):
            raise SyntaxError("Not a valid Python code")
        return source
    except HTTPError:
        return None
    except SyntaxError:
        return None