from __future__ import print_function
import subprocess


class ShellExecutor():

    def __init__(self):
        self.process = None

    def __enter__(self):
        self.process = subprocess.Popen(['/bin/bash', ], shell=True,
                                        stdin=subprocess.PIPE,
                                        stdout=subprocess.PIPE)
        return self

    def __exit__(self, type, value, traceback):
        self.process.stdin.close()
        self.process.wait()

    def run_command(self, command):
        wrapped_command = "{}; echo END\n".format(command)
        self.process.stdin.write(wrapped_command.encode())
        self.process.stdin.flush()
        return self.process.stdout.readline().decode().strip()

def dummy():
    process = subprocess.Popen(['/bin/cat'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE)
    process.stdin.write(b'Hello\n')
    process.stdin.flush()
    print(repr(process.stdout.readline())) # Should print 'Hello\n'
    process.stdin.write(b'World\n')
    process.stdin.flush()  
    print(repr(process.stdout.readline())) # Should print 'World\n'

    # "cat" will exit when you close stdin.  (Not all programs do this!)
    process.stdin.close()
    print('Waiting for cat to exit')
    process.wait()
    print('exit')


if __name__ == "__main__":
    dummy()


    cmds = ["echo export MY_VARIABLE='hello world'",
            "cd wyriwyd/",
            "pwd",
            "echo MY_VARIABLE = '$MY_VARIABLE'"]

    with ShellExecutor() as executor:
        for command in cmds:
            output = executor.run_command(command)
            print(output)
