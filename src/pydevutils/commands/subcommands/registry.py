from pathlib import Path
from importlib import import_module

registry = {}


def register_command(name):
    def inner(cls):
        if name not in registry:
            registry.update({name: cls})
        return

    return inner


class CommandImplementation:
    """
    Base class for all command args
    """

    def setup_parser(self, parser):
        raise NotImplementedError("setup_parser not implemented")

    def handle_command(self, arg):
        raise NotImplementedError("handle_command not implemented")


# looks at all the files in the directory to automagically import them
# so that they register themselves.

whereami = Path(__file__).parent

for d in whereami.iterdir():
    ignore_list = ["registry.py", "__init__.py"]
    if d.name.endswith(".py"):
        if d.name not in ignore_list:
            module_name = d.name.rstrip(".py")
            module_full_path = (
                f"pydevutils.commands.subcommands.{module_name}"
            )
            import_module(module_full_path)
