import ast
import importlib.abc
import importlib.machinery
import sys
import logging
import requests

from .utils import is_valid_python_code

class CloudFinder(importlib.abc.MetaPathFinder):
    def __init__(self, base_url: str):
        self.base_url = base_url
    
    def find_spec(self, fullname, path, target=None):
        spec = self._find_py_file_spec(fullname)
        if spec is not None: return spec
        spec = self._find_package_init_spec(fullname)
        return spec if spec is not None else None
    
    def _find_py_file_spec(self, fullname: str):
        url = f"{self.base_url}/{fullname.replace(".", "/")}.py"
        source = self._get_remote_python_source(url)
        if source is None: return None
        loader = CloudLoader(fullname, source, url)
        return importlib.machinery.ModuleSpec(fullname, loader, origin=url)
