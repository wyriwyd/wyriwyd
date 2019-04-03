
from pygments import highlight
from pygments.lexers import DiffLexer
from pygments.formatters import Terminal256Formatter

from .parser import parse_file
from .checker import check_commands

import logging
logger = logging.getLogger(__name__)
logger.setLevel("INFO")


def prepare_parser():
    from argparse import ArgumentParser
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("infile", help="The path to the input markdown file")
    parser.add_argument("-r", "--raise-error", default=False, action="store_true",
                        help="Raise an exception at the first error")
    parser.add_argument("-e", "--empty", help="""If the Markdown file contains
commands without a following output, and the command when runs
produces output, treat this as an error""")
    return parser


def main(args=None):
    args = prepare_parser().parse_args(args=args)
    commands = parse_file(args.infile)
    errors = check_commands(commands,
                            no_expected_means_empty_out=args.empty,
                            raise_error=args.raise_error)
    if not errors:
        print("Everything looks ok!!")
        return 0

    for error in errors:
        print(highlight(error, DiffLexer(), Terminal256Formatter()))
    return 1
