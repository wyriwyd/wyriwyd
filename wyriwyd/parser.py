from __future__ import print_function
import mistletoe
from mistletoe.block_token import CodeFence


def parse_file(filename):
    """
    Open a markdown file and return a list of shell commands and outputs
    """
    with open(filename, "r") as infile:
        return parse_string(infile)


def parse_string(document):
    contents = mistletoe.Document(document)
    blocks = [block for block in contents.children if isinstance(block, CodeFence)]
    command_output_pairs = group_blocks(blocks)
    return command_output_pairs


def get_content(block):
    return block.children[0].content.strip()


def group_blocks(blocks):
    pairs = []
    current_command = None
    for block in blocks:
        language = block.language
        content = get_content(block)
        if language == "bash":
            if current_command:
                pairs.append((current_command, None))
            current_command = content
        elif language == "output":
            if not current_command:
                raise RuntimeError("Output without a command to produce it")
            pairs.append((current_command, content))
            current_command = None
    if current_command:
        pairs.append((current_command, None))
    return pairs
