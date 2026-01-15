import os
from utils import log_function_call


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
