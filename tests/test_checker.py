import os
from wyriwyd.checker import check_commands

def test_checker(tmpdir):
    cmds = ["export MY_VARIABLE='hello world'",
            "cd {}".format(str(tmpdir)),
            "pwd",
            "echo MY_VARIABLE = $MY_VARIABLE",
            "pushd ../ \n pwd \n popd"]
    outputs= [None, None, str(tmpdir)]
    outputs+= ["MY_VARIABLE = hello world"]
    cmd_out = "{0} {1}\n{0}\n{1}"
    cmd_out = cmd_out.format(os.path.dirname(tmpdir), str(tmpdir))
    outputs += [cmd_out]

    check_commands(list(zip(cmds, outputs)))
