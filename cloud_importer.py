from sys import meta_path
from .cloud_finder import CloudFinder
from typing import Callable

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

add_github_repo: Callable = add_git_repo
