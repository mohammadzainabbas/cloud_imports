from importlib.abc import Loader
from importlib.machinery import ModuleSpec
import sys, logging

class CloudLoader(Loader):
    
    def __init__(self, fullname: str, source_code: str, url: str) -> None:
        self.fullname = fullname
        self.source_code = source_code
        self.url = url

    def create_module(self, spec):
        modules = sys.modules.get(self.fullname)
        return None
