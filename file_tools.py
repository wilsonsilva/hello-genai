import os
from functools import wraps


def log_function_call(func):
    """Decorator that logs function calls with their arguments."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        # Format arguments
        arg_strs = [repr(arg) for arg in args]
        kwarg_strs = [f"{k}: {v!r}" for k, v in kwargs.items()]
        all_args = ", ".join(arg_strs + kwarg_strs)

        print(f"[Function Call] {func.__name__}({all_args})")
        return func(*args, **kwargs)

    return wrapper


@log_function_call
def read_file(file_path: str) -> str:
    """Reads a file and returns its contents.

    Args:
        file_path: Path to the file to read.
    """
    with open(file_path, "r") as f:
        return f.read()


@log_function_call
def write_file(file_path: str, contents: str) -> bool:
    """Writes a file with the given contents.

    Args:
        file_path: Path to the file to write.
        contents: Contents to write to the file.
    """
    with open(file_path, "w") as f:
        f.write(contents)
    return True


@log_function_call
def list_dir(directory_path: str) -> list[str]:
    """Lists the contents of a directory.

    Args:
        directory_path: Path to the directory to list.
    """
    full_path = os.path.expanduser(directory_path)
    return os.listdir(full_path)


# List of available file tools
file_tools = [read_file, write_file, list_dir]
