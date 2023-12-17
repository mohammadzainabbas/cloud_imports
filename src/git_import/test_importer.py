from .git_importer import GithubRepo, add_repo, add_github_repo, extract_github_info

def main():
    gh_repo = GithubRepo(username="mohammadzainabbas", repo="cloud_imports", branch="main")
    add_github_repo("https://github.com/pandas-dev/pandas")
    print(gh_repo)

if __name__ == "__main__":
    main()