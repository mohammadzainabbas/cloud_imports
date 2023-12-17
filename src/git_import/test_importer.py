from src.git_import.git_importer import GithubRepo, add_repo, add_github_repo, extract_github_info

def main():
    gh_repo = GithubRepo(username="mohammadzainabbas", repo="cloud_imports", branch="main")
    add_github_repo("https://github.com/kiranmantri/python-remote-import")
    import pandas as pd
    print(pd.__version__)
    print(gh_repo)

if __name__ == "__main__":
    main()