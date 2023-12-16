from sys import meta_path
from .cloud_finder import CloudFinder

def add_repo(repo_url: str | None) -> None:
    """
    Add a repository to `sys.meta_path`
    """
    meta_path.append(CloudFinder(repo_url))

def add_github_repo(repo_url: str | None) -> None:
    """
    Add a github repository to `sys.meta_path`

    Example:
    ```python
    add_github_repo("https://github.com/mohammadzainabbas/cloud_imports")
    ```

    This will add the repository `

    
    """
    add_repo(repo_url)

