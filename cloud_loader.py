from importlib.abc import Loader
from importlib.machinery import ModuleSpec
import sys, logging, 
from types import ModuleType

class CloudLoader(Loader):
    
    def __init__(self, fullname: str, source_code: str, url: str) -> None:
        self.fullname = fullname
        self.source_code = source_code
        self.url = url

    def create_module(self, spec: ModuleSpec | None = None) -> None:
        module = sys.modules.get(spec.name)
        if module is None:
            module = ModuleType(spec.name)
            sys.modules[spec.name] = module
        return module
    
    def exec_module(self, module: ModuleType) -> None:
        
        exec(self.source_code, module.__dict__)
