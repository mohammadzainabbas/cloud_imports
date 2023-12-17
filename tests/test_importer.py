from git_import.git_importer import GithubRepo, add_repo, add_github_repo, extract_github_info

def main():
    GithubRepo(username="mohammadzainabbas", repo="cloud_imports", branch="main")

if __name__ == "__main__":
    main()