import ast
import importlib.abc
import importlib.machinery
import sys
import logging
import requests

from .utils import is_valid_python_code

class CloudFinder(importlib.abc.MetaPathFinder):
    def __init__(self, cloud_url):
        self.cloud_url = cloud_url