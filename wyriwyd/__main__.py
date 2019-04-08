
from pygments import highlight
from pygments.lexers import DiffLexer
from pygments.formatters import Terminal256Formatter

from .parser import parse_file
from .checker import check_commands
from .interactive import make_doc_from_session

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


def prepare_parser_wizard():
    from argparse import ArgumentParser
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("-o", "--outfile", default=None,
                        help="The path to the output markdown documentation")
    parser.add_argument("-a", "--append", default=False, action="store_true",
                        help="Append to existing documentation, rather than overwrite it")
    parser.add_argument("-s", "--skip-blank-output", default=False, action="store_true",
                        help="""If a command prints no output, don't add a blank \
output section to the documentation""")
    return parser


def main_wizard(args=None):
    args = prepare_parser_wizard().parse_args(args=args)
    make_doc_from_session(**vars(args))
    return 0
