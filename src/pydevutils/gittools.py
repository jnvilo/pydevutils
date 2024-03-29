import os
import sys
import argparse
from pathlib import Path
from github import Github
from git import Repo

from os.path import expanduser


def is_git_repo(path):
    path = Path(path, ".git")

    return path.is_dir()


def make_github_repo():
    args = get_args()
    path = os.getcwd()

    if not is_git_repo(path):
        bare_repo = Repo.init(path, bare=True)
        print(bare_repo)


class GitHubToken(object):
    def __init__(self):
        pass

    @property
    def token(self):
        path = Path(expanduser("~"), ".config/pydevtools")
        return self._load_token(path)

    def _load_token(self, path):
        path = Path(path)
        if not path.exists():
            # create only if the homedir is valid path
            if Path(expanduser("~")).exists():
                path.mkdir(parents=True, exist_ok=True)
            else:
                print(
                    "PyDevtools home dir does not exist! Could not create {}".format(
                        path
                    )
                )

        token_path = Path(path, "token.txt")

        try:
            with open(token_path.as_posix(), "r") as f:
                token_str = f.read()
                return token_str.rstrip("\n")
        except FileNotFoundError as e:
            print("Token file {} was not found. Please create it.")
            sys.exit(1)

    def __str__(self):
        return self.token


class GitHub(object):
    def __init__(self, token=None):
        if token == None:
            token = GitHubToken()
            token = token.token.rstrip("\n")

        github = Github(token)
        self.user = github.get_user()

    def get_repos(self):
        return self.user.get_repos()

    @property
    def repos(self):
        return self.get_repos()


class GitHubRepo(GitHub):
    def __init__(self, path=None, name=None, token=None):
        self._path = path
        self._name = name
        self._local_repo = None

        super()

    @property
    def name(self):
        if self._name == None:
            # get the name from the path
            self._name = Path(self.path).name
        return self._name

    @property
    def path(self):
        return Path(self._path)

    def __has_dotgit(self, path):
        """
        Checks if the current path is a git repo. It does this
        recursively checking the parent directories.
        """

        dot_git_path = Path(path, ".git")
        result = False

        if not dot_git_path.is_dir():
            if dot_git_path.parent == path:
                result = False
            else:
                parent_path = path.parent
                result = self.__has_dotgit(parent_path)
        else:
            result = True

        return result

    @property
    def is_gitrepo(self):
        """
        Returns true if we are inside a git repo
        """

        # recursively look for a .git
        return self.__has_dotgit(self.path)

    @property
    def local_repo(self):
        if self._local_repo == None:
            self._local_repo, _ = self.make_local_repo()
        return self._local_repo

    def make_local_repo(self):
        """
        Creates a local repo. Same as doing git init
        """

        if not self.is_gitrepo:
            repo = Repo.init(path=self.path)
            return repo, True
        else:
            ##
            # TODO: This works only if the self.path is
            # actually where .git exists in.
            #
            # The fix is that self.path must be adjusted
            # to point always to where .git is
            ##
            repo = Repo(path=self.path)

        return repo, False

    @property
    def has_github_repo_as_remote(self):
        """
        Checks if the local repo has a remote set already
        """

    @property
    def github_repo(self):
        # if self._github_repo does not exist then we need to find
        # out if the local repo already has a remote set.

        if not self.has_github_repo_as_remote:
            pass

    def make_github_repo(self):
        """
        Creates a remote github repo
        """
        token = GitHubToken()
        github = Github(token.token.rstrip("\n"))
        user = github.get_user()
        repo = user.create_repo(self.name)

        self._github_repo = repo

        return repo

    def set_remote_to_github(self):
        url = "git@github.com:jnvilo/{}.git".format(self.name)
        remote = repo.create_remote("origin", url=url)

        return remote


if __name__ == "__main__":
    make_github_repo()
