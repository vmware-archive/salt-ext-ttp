def test_doc_no_match(salt_call_cli):
    """
    Test that a non existing module does not show up in docs output
    """
    ret = salt_call_cli.run("-d", "monty.python")
    assert ret.exitcode == 0
    # Nothing should be printed by salt
    assert not ret.stdout


def test_doc(salt_call_cli):
    ret = salt_call_cli.run("-d", "ttp.run")
    assert ret.exitcode == 0
    # If we get the right doc, salt succeeded in loading our plugin and using it through
    # setuptools entry-points
    assert "ttp.run:" in ret.stdout
    assert (
        "Function to run TTP Templates retrieving data using SALT execution modules" in ret.stdout
    )
