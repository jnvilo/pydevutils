from .registry import register_command
from .registry import CommandImplementation

from pydevutils.gittools import make_github_repo

@register_command("github")
class GitHubCommand(CommandImplementation):

    @classmethod
    def setup_parser(self, parent_parser):
        github_parser = parent_parser.add_parser("github", help="GitHub command")
        github_commands = github_parser.add_subparsers(dest="subcommand")
        createrepo_command_parser = github_commands.add_parser("createrepo", help="Create a github repo")
        return github_parser

    def handle_command(self, args):
        print("Handling GitHub command")
        print(args)

        if args.subcommand == "createrepo":
            print("creating repo")



    def list_github_repos(self):
        gt = GitTools()
        repos = gt.list_github_repos()
        for repo in repos:
            print(repo)
