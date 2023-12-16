from importlib.abc import Loader
from importlib.machinery import ModuleSpec
import sys, logging

class CloudLoader(Loader):
    
    def __init__(self, fullname: str, source_code: str, url: str) -> None:
        self.fullname = fullname
        self.source_code = source_code
        self.url = url

    def create_module(self, spec: ModuleSpec | None = None) -> None:
        module = sys.modules.get(spec.name)
        if module is None:
