from importlib.abc import MetaPathFinder
from importlib.abc import LazyLoader
from importlib.machinery import ModuleSpec
import sys, logging
import requests
from typing import Any

from .cloud_loader import CloudLoader
from .utils import get_remote_python_source

class CloudFinder(MetaPathFinder):

    def __init__(self, base_url: str) -> None:
        self.base_url = base_url
    
    def find_spec(self, fullname: str | Any, path: Any, target: Any | None = None) -> (ModuleSpec | None):
        spec = self._find_py_file_spec(fullname)
        if spec is not None: return spec
        spec = self._find_package_init_spec(fullname)
        return spec if spec is not None else None
    
    def _find_py_file_spec(self, fullname: str):
        url = f"{self.base_url}/{fullname.replace(".", "/")}.py"
        source = get_remote_python_source(url)
        if source is None: return None
        loader = CloudLoader(fullname, source, url)
        return ModuleSpec(fullname, loader, origin=url)
    
    def _find_package_init_spec(self, fullname: str):
        url = f"{self.base_url}/{fullname.replace('.', '/')}/__init__.py"
        source = get_remote_python_source(url)
        if source is None: return None
        loader = CloudLoader(fullname, source, url)
        return ModuleSpec(fullname, loader, origin=url, is_package=True)
    