from sys import meta_path

def add_repo(repo_url: str) -> None:
    """Add a repository to sys.meta_path"""
    meta_path.append(CloudFinder(repo_url))