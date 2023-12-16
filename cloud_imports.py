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
        if path is None:
            path = ['']
        if path[0] != '':
            return None
        logging.debug(f'find_spec({fullname!r}, {path!r}, {target!r})')
        spec = self._find_spec(fullname, path)
        logging.debug(f'find_spec({fullname!r}, {path!r}, {target!r}) -> {spec!r}')
        return spec
    