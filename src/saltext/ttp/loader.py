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
