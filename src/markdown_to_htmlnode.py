from block_delimeter import *
from delimiter import *
from textnode import *
from htmlnode import *

def markdown_to_htmlnode(mkd):
    blocks = markdown_to_blocks(mkd)
    nodes = []
    for block in blocks:
        block_to_node

def block_to_node(block, block_type):
    match block_type:
        case "paragraph":
            return ParentNode("p",[text_to_children(block)],None)
        case "code": 
            codenode = TextNode(block, TextType.PLAIN)
            return ParentNode("code",text_node_to_html_node(codenode),None)
        case "unordered list":
            return ParentNode("ul", , None)
        case "ordered list":
            return ParentNode("ol", , None)
        case "quote":
            return ParentNode("blockquote", [text_to_children(block)], None)
        case "heading":
            i = 0
            while True:
                ++i
                if block[i] != "#":
                    break
            return ParentNode(f"h{i}", [text_to_children(block)], None)

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))
    return html_nodes
