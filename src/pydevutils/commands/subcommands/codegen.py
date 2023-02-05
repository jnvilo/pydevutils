import ast
from .registry import register_command
from .registry import CommandImplementation

from pydevutils.moduletools import get_classes
@register_command("codegen")
class GitHubCommand(CommandImplementation):

    @classmethod
    def setup_parser(self, parent_parser):
        github_parser = parent_parser.add_parser("codegen", help="Code generation tools")
        github_commands = github_parser.add_subparsers(dest="subcommand")
        list_classes_cmd_parser = github_commands.add_parser("list-classes", help="List the classes in a module")
        list_classes_cmd_parser.add_argument("--file", "-f", help="The file to list classes from")
        return github_parser

    def handle_command(self, args):

        if args.subcommand == "list-classes":
            if args.file:
                print(args.file)
                classes = get_classes(args.file)
                print(classes)
            else:
                print(args.help)


