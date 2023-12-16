from importlib.abc import MetaPathFinder
from importlib.machinery import ModuleSpec
import sys, logging
import requests
from typing import Any
from .utils import is_valid_python_code

class CloudFinder(MetaPathFinder):
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url
    
    @classmethod
    def find_spec(self, fullname: str | Any, path: Any, target: Any | None = None) -> (ModuleSpec | None):
        spec = self._find_py_file_spec(fullname)
        if spec is not None: return spec
        spec = self._find_package_init_spec(fullname)
        return spec if spec is not None else None
    
    def _find_py_file_spec(self, fullname: str):
        url = f"{self.base_url}/{fullname.replace(".", "/")}.py"
        source = self._get_remote_python_source(url)
        if source is None: return None
        loader = CloudLoader(fullname, source, url)
        return ModuleSpec(fullname, loader, origin=url)
    
    def _find_package_init_spec(self, fullname: str):
        url = f"{self.base_url}/{fullname.replace('.', '/')}/__init__.py"
        source = self._get_remote_python_source(url)
        if source is None: return None
        loader = CloudLoader(fullname, source, url)
        return ModuleSpec(fullname, loader, origin=url, is_package=True)
    
    def _get_remote_python_source(self, url: str) -> str | None:
        try:
            response = requests.get(url)
            response.raise_for_status()
            source = response.text
            if not is_valid_python_code(source):
                raise SyntaxError("Not a valid Python code")
            return source
        except requests.exceptions.HTTPError:
            return None
        except SyntaxError:
            return None