import ast

def get_child_classes( file_path, base_class=None):
    """
    Get all child classes of a base class in a file. This can be usefull for example in creating an __all__
    variable in a module instead of manually listing all the classes. This function will return a list of class names.
    :param file_path:
    :param base_class:
    :return:
    """
    child_classes = []
    with open(file_path, 'r') as f:
        tree = ast.parse(f.read())
    for node in ast.walk(tree):

        if isinstance(node, ast.ClassDef):
            if base_class:
                if has_base_class(node, base_class):
                    child_classes.append(node.name)
            else:
                child_classes.append(node.name)

    return child_classes

def has_base_class(node, base_class):
    for base in node.bases:
        if isinstance(base, ast.Name) and base.id == base_class.__name__:
            return True
    return False

def get_all_classes(file_path):
    all_classes = []
    with open(file_path, 'r') as f:
        tree = ast.parse(f.read())
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            all_classes.append(node.name)
    return all_classes
def get_classes(file_path):
    """Get all classes in a file. This can be usefull for example in creating an __all__
    variable in a module. This function will return a list of class names."""

    child_classes = get_child_classes(file_path)
    return child_classes

if __name__ == "__main__":
    from pydevutils.commands.subcommands.codegen import CommandImplementation
    print(get_child_classes("/pydevutils/commands/subcommands/codegen.py", base_class=CommandImplementation))