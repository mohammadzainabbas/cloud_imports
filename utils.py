import ast

def is_valid_python_source(source):
    try:
        ast.parse(source)
    except SyntaxError:
        return False
    return True