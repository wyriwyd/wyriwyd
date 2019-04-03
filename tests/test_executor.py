import os
from wyriwyd.executor import ShellExecutor


def test_executor(tmpdir):
    cmds = ["export MY_VARIABLE='hello world'",
            "cd {}".format(str(tmpdir)),
            "pwd",
            "echo MY_VARIABLE = $MY_VARIABLE",
            "pushd ../ \n pwd \n popd"]

    outputs = []
    with ShellExecutor() as executor:
        for command in cmds:
            outputs.append(executor.run_command(command))
    assert outputs[:3] == [[], [], [str(tmpdir)]]
    assert outputs[3] == ["MY_VARIABLE = hello world"]
    cmd_out = "{0} {1}:{0}:{1}"
    cmd_out = cmd_out.format(os.path.dirname(tmpdir), str(tmpdir))
    assert outputs[4] == cmd_out.split(":")
