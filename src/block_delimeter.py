from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    U_LIST = "unordered list"
    O_LIST = "oredered list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    new_blocks = []
    for block in blocks:
        if block.strip() != "":
            new_blocks.append(block.strip())    
    return new_blocks

def block_to_block_type(mkd_text):
    if re.match(r"#{1,6} ",mkd_text):
        return BlockType.HEADING
    elif bool(re.match(r"```\n", mkd_text)) and re.search(r"```$",mkd_text):
        return BlockType.CODE
    elif re.search(r"^>", mkd_text, re.MULTILINE):
        return BlockType.QUOTE
    elif re.search(r"^- ", mkd_text, re.MULTILINE):
        return BlockType.U_LIST
    elif re.search(r"^\d+\.", mkd_text, re.MULTILINE) and mkd_text[:2] == "1.":
        return BlockType.O_LIST
    else:
        return BlockType.PARAGRAPH

