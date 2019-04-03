from __future__ import print_function
import subprocess


COMMAND_ENDED_STRING = "END COMMAND slufhaspidfha" * 5


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
        wrapped_command = "{}; echo {}\n".format(command, COMMAND_ENDED_STRING)
        self.process.stdin.write(wrapped_command.encode())
        self.process.stdin.flush()
        lines = []
        while True:
            last_line = self.process.stdout.readline().decode()[:-1]
            if last_line == COMMAND_ENDED_STRING:
                break
            lines.append(last_line)
        return lines
