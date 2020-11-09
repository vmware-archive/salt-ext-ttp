import os

import pytest
from saltext.ttp import PACKAGE_ROOT
from saltfactories.utils import random_string


@pytest.fixture(scope="session")
def salt_factories_config():
    """
    Return a dictionary with the keyworkd arguments for FactoriesManager
    """
    return {
        "code_dir": str(PACKAGE_ROOT),
        "inject_coverage": "COVERAGE_PROCESS_START" in os.environ,
        "inject_sitecustomize": "COVERAGE_PROCESS_START" in os.environ,
        "start_timeout": 120 if os.environ.get("CI") else 60,
    }


@pytest.fixture(scope="package")
def master(request, salt_factories):
    factory = salt_factories.get_salt_master_daemon(random_string("master-"))
    with factory.started():
        yield factory


@pytest.fixture(scope="package")
def minion(request, master):
    factory = master.get_salt_minion_daemon(random_string("minion-"))
    with factory.started():
        yield factory


@pytest.fixture
def salt_run_cli(master):
    return master.get_salt_run_cli()


@pytest.fixture
def salt_cli(master):
    return master.get_salt_cli()


@pytest.fixture
def salt_call_cli(minion):
    return minion.get_salt_call_cli()
