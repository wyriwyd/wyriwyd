from six.moves import input
from .executor import ShellExecutor


COMMAND_BLOCK = """\
```bash
{cmd}
```
"""


OUTPUT_BLOCK = """\
```output
{output}
```
"""


class InteractiveSession():
    def __init__(self, filename, append=False):
        self.file = None
        self.mode = "a" if append else "w"
        if filename:
            self.filename = filename
        else:
            self.filename = input("Output file name (.md):")

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        self.file.__enter__()
        return self

    def __exit__(self, cls, value, traceback):
        self.file.__exit__(cls, value, traceback)

    def __iter__(self):
        lines = []
        ps1 = "$ "
        ps2 = "> "
        prompt = ps1
        while True:
            try:
                cmd = input(prompt).strip()
            except EOFError:
                break
            if not cmd or cmd == "exit":
                break
            lines.append(cmd)
            prompt = ps2
            if cmd[-1] != '\\':
                yield "\n".join(lines)
                lines = []
                prompt = ps1

    def store_command(self, cmd):
        self.file.write(COMMAND_BLOCK.format(cmd=cmd))

    def store_output(self, out):
        self.file.write(OUTPUT_BLOCK.format(output=out))


def make_doc_from_session(outfile, append=False, skip_blank_output=True):
    with InteractiveSession(outfile, append) as session, ShellExecutor() as executor:
        for cmd in session:
            session.store_command(cmd)
            output = executor.run_command(cmd)
            output = "\n".join(output)
            if output or not skip_blank_output:
                print(output)
                session.store_output(output)
