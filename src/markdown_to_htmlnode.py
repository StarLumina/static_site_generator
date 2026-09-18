from block_delimeter import *
from delimiter import *
from textnode import *
from htmlnode import *

def markdown_to_html_node(mkd):
    blocks = markdown_to_blocks(mkd)
    nodes = []
    for block in blocks:
        typeOfBlock = block_to_block_type(block)
        newNodes = block_to_node(block, typeOfBlock)
        nodes.append(newNodes)
    return ParentNode("div", nodes, None)
        

def block_to_node(block, block_type):
    match block_type:
        case BlockType.PARAGRAPH:
            return ParentNode("p", text_to_children(block.replace("\n", " ")),None)
        case BlockType.CODE: 
            chopped_block = block[4:-3]
            codenode = TextNode(chopped_block, TextType.PLAIN)
            return ParentNode("pre",[ParentNode("code",[text_node_to_html_node(codenode)],None)], None)
        case BlockType.U_LIST:
            return ParentNode("ul", wrap_lists(block, "ul"), None)
        case BlockType.O_LIST:
            return ParentNode("ol", wrap_lists(block, "ol"), None)
        case BlockType.QUOTE:
            split_quotes = block.split("\n")
            quotes = []
            for quote in split_quotes:
                quotes.append(quote[2:])
            return ParentNode("blockquote", text_to_children(" ".join(quotes)), None)
        case BlockType.HEADING:
            i = 0
            while True:
                i += 1
                if block[i] != "#":
                    break
            return ParentNode(f"h{i}", text_to_children(block[i+1:]), None)
        case _:
            raise ValueError(f"unknown block type:{block_type}")

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))
    return html_nodes

def wrap_lists(text, type):
    listText = text.split("\n")
    children = []
    for l in listText:
        if type == "ul":
            l = l[2:]
        else:
            l = l.split(". ")[1]
        child = text_to_children(l)
        children.append(ParentNode("li", child, None))
    return children
    
