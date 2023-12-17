from src.git_import.git_importer import GithubRepo, add_repo, add_github_repo, extract_github_info

def main():
    gh_repo = GithubRepo(username="mohammadzainabbas", repo="cloud_imports", branch="main")
    print(gh_repo)

    # add_github_repo("https://github.com/kiranmantri/python-remote-import")
    # from remote_import import RemoteImporter

    # r = RemoteImporter.add_remote(
    #     namespaces=["test_package"],
    #     base_url ='github://kiranmantri:python-remote-import@/examples'
    #     )
    # print(r)

if __name__ == "__main__":
    main()