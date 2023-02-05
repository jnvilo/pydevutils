import sys
import argparse

""" Implements upcloud command line interface"""
from pydevutils.commands.subcommands.registry import registry


def main():
    description = "pydevtools CLI"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--version", action="version", version="%(prog)s 0.1")

    subparsers = parser.add_subparsers(dest="command")

    for cmd_name in registry:
        Klass = registry[cmd_name]
        Klass.setup_parser(subparsers)

    args = parser.parse_args()
    cmd_klass = registry.get(args.command, None)

    if cmd_klass is not None:
        cmd = cmd_klass()
        cmd.handle_command(args)
    else:
        parser.print_help(sys.stderr)

if __name__ == "__main__":
    main()