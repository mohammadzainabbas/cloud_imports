from sys import meta_path
from urllib.parse import urlparse
from .cloud_finder import CloudFinder

from dataclasses import dataclass

@dataclass
class GithubRepo:
    username: str
    repo: str
    branch: str = 'main'
    
    @property
    def url(self) -> str:
        return f"https://raw.githubusercontent.com/{self.username}/{self.repo}/{self.branch}"

    def __str__(self) -> str:
        return self.url

    def __repr__(self) -> str:
        return f"GithubRepo(username={self.username}, repo={self.repo}, branch={self.branch})"

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

def extract_github_info(url: str, branch: str = 'main'):
    """
    Extracts the username, repository, and branch from a GitHub URL.

    If no branch is specified in the URL, `main` is returned as the default branch.

    Parameters:
    url (str): The GitHub URL.

    Returns:
    dict: A dictionary containing the 'username', 'repo', and 'branch'.
    """
    parsed_url = urlparse(url)
    path_parts = parsed_url.path.strip("/").split("/")

    username = path_parts[0] if len(path_parts) > 0 else None
    repo = path_parts[1] if len(path_parts) > 1 else None
    branch = path_parts[3] if len(path_parts) > 3 else branch

    return {"username": username, "repo": repo, "branch": branch}