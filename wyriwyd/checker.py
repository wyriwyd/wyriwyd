from .executor import ShellExecutor
import logging
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
                msg = f"Output not matching expectationg for cmd '''{command}'''"
                full = msg + f"\n\nExpected:\n{expected}\n\nReceived:\n{output}"
                if raise_error:
                    logger.error(full)
                    raise OutputDoesntMatchExpectation(msg)
                errors.append(full)
    return errors
