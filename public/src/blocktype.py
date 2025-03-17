import re

from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    heading_regex_pattern = r"^(#{1,6} ).*"
    code_regex_pattern = r"^(\`{3}).*(\`{3})$"
    quote_regex_pattern = r"^>.*(\n>.*)*$"

    if re.match(heading_regex_pattern, block):
        return BlockType.HEADING
    elif re.match(code_regex_pattern, block, re.DOTALL):
        return BlockType.CODE
    elif re.match(quote_regex_pattern, block, re.DOTALL):
        return BlockType.QUOTE
    elif _is_unordered_list(block):
        return BlockType.UNORDERED_LIST
    elif _is_ordered_list(block):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH

def _is_unordered_list(block):
    for line in block.split('\n'):
        if not line.startswith(f"- "):
            return False
    return True

def _is_ordered_list(block):
    count = 0
    for line in block.split('\n'):
        count += 1
        if not line.startswith(f"{count}. "):
            return False
    return True