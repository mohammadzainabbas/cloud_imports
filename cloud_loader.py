from importlib.abc import Loader
import sys, logging

class CloudLoader(Loader):
    
    def __init__(self) -> None:
        super().__init__()