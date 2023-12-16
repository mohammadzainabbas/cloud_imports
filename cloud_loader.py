from importlib.abc import Loader
import sys, logging

class CloudLoader(Loader):
    
    def __init__(self, fullname, source_code, url) -> None:
