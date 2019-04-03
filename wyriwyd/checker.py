from .executor import ShellExecutor
import logging
logger = logging.getLogger(__name__)


class OutputWasntExpected(Exception):
    pass


class OutputDoesntMatchExpectation(Exception):
    pass


# class CommandFailed(Exception):
#     pass


def check_commands(commands, no_expected_means_empty_out=True):
    with ShellExecutor() as executor:
        for command, expected in commands:
            output = executor.run_command(command)
            output = "\n".join(output)
            if expected is None and no_expected_means_empty_out and output:
                msg = f"Unexpected output for cmd '''{command}'''"
                raise OutputWasntExpected(msg)
            if expected is None:
                continue
            if output != expected:
                msg = f"Output not matching expectationg for cmd '''{command}'''"
                logger.error(msg + "\n Expected:\n%s\nReceived:\n%s", expected, output)
                raise OutputDoesntMatchExpectation(msg)



if __name__ == "__main__":
    from .parser import parse_file
    commands = parse_file("examples/sample.md")
    check_commands(commands)
