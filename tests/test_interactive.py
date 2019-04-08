import os
import sys
import pytest
from contextlib import contextmanager
from wyriwyd.interactive import make_doc_from_session
from io import StringIO


@contextmanager
def replace_streams(instream=None, outstream=None, errstream=None):
    inorig = sys.stdin
    outorig = sys.stdout
    errorig = sys.stderr
    if instream:
        sys.stdin = instream
    if outstream:
        sys.stdout = outstream
    if errstream:
        sys.stderr = errstream
    yield
    sys.stdin = inorig
    sys.stdout = outorig
    sys.stderr = errorig

def test_make_doc_from_session(tmpdir):
    cmds = ["export MY_VARIABLE='hello world'",
            "cd {}".format(str(tmpdir)),
            "pwd",
            "echo MY_VARIABLE = $MY_VARIABLE",
            "pushd ../ && \ \n pwd && \ \n popd",
            "exit"]
    instream = StringIO("\n".join(cmds))
    outstream = StringIO()
    with replace_streams(instream=instream, outstream=outstream):
        make_doc_from_session(str(tmpdir / "dummy.md"), append=True)
    # print(outstream.getvalue())
    lines = (tmpdir / "dummy.md").read()
    # print(lines)
    expect = ["", "", "", str(tmpdir) + "\n"]
    expect += ["MY_VARIABLE = hello world\n"]
    expect += ["> > {0} {1}\n{0}\n{1}\n".format(os.path.dirname(str(tmpdir)), str(tmpdir))]
    expect += [""]
    assert outstream.getvalue() == "$ ".join(expect)
    # assert False
