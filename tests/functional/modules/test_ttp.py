import pytest
import salt.loader


@pytest.fixture(scope="module")
def loader(minion):
    return salt.loader.minion_mods(minion.config)


def test_loader_no_match(loader):
    """
    Test that a non existing module does not show up in the loader
    """
    assert "monty.python" not in loader


def test_loader(loader):
    """
    Test that our module is loaded
    """
    assert "ttp.run" in loader
