from sys import meta_path
from .cloud_finder import CloudFinder
from typing import Callable
from functools import partial, partialmethod

def add_repo(repo_url: str | None) -> None:
    """
    Add a repository to `sys.meta_path`
    """
    meta_path.append(CloudFinder(repo_url))

def add_git_repo(repo_url: str | None) -> None:
    """
    Add a git repository to `sys.meta_path`
    """
    add_repo(repo_url)

add_github_repo: Callable = partialmethod(add_git_repo)