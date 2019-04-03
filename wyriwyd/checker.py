import logging
from difflib import ndiff

from .executor import ShellExecutor

logger = logging.getLogger(__name__)


class OutputWasntExpected(Exception):
    pass


class OutputDoesntMatchExpectation(Exception):
    pass


# class CommandFailed(Exception):
#     pass


def check_commands(commands, no_expected_means_empty_out=True, raise_error=True):
    errors = []
    with ShellExecutor() as executor:
        for command, expected in commands:
            #print("Running command", command)
            output = executor.run_command(command)
            output = "\n".join(output)
            if expected is None and no_expected_means_empty_out and output:
                msg = f"Unexpected output for cmd '''{command}'''"
                if raise_error:
                    raise OutputWasntExpected(msg)
                errors.append(msg)
            if expected is None:
                continue
            if output != expected:
                full = [f"@@ Output not matching expectation for cmd '''{command}'''@@"]
                full += [
                    line.strip("\n")
                    for line in ndiff(output.splitlines(True), expected.splitlines(True))
                ]
                errors += full
                if raise_error:
                    logger.error(full)
                    raise OutputDoesntMatchExpectation(msg)
    return errors
