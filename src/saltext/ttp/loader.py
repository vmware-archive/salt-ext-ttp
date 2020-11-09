"""
Define the required entry-points functions in order for Salt to know
what and from where it should load this plugin's loaders
"""
from . import PACKAGE_ROOT


def module_dirs():
    """
    Return a list of paths from where salt should load execution modules
    """
    return [str(PACKAGE_ROOT / "modules")]


def runner_dirs():
    """
    Return a list of paths from where salt should load runner modules
    """
    return [str(PACKAGE_ROOT / "runners")]
