"""
Common utility validators required for the commands
"""
import pathlib


def is_valid_python_classname(name: str):
    """ Returns boolean indicating whether name is a valid Python identifier

    Parameters
    ----------
    name : str
        A string representing a class name

    Returns
    -------
    bool
        True when name is a valid python identifier, False otherwise
    """
    return str.isidentifier(name)


def is_file_exist(name: str):
    """ Returns boolean indicating whether a file exists at path indicated by name

    Parameters
    ----------
    name : str
        String representing filename

    Returns
    -------
    bool
        True when filename indicated by name exists, False otherwise
    """
    path = pathlib.Path(name)
    return path.is_file()
