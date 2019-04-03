import pytest
from wyriwyd.executor import ShellExecutor


def test_executor(tmpdir):
    cmds = ["export MY_VARIABLE='hello world'",
            "cd {}".format(str(tmpdir)),
            "pwd",
            "echo MY_VARIABLE = $MY_VARIABLE"]

    outputs = []
    with ShellExecutor() as executor:
        for command in cmds:
            outputs.append(executor.run_command(command))
    assert outputs == [[], [], [str(tmpdir)], ["MY_VARIABLE = hello world"]]
