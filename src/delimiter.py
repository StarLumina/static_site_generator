from textnode import *
from htmlnode import * 
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes= []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue
        split = []
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0: 
            raise Exception("Invalid Markdown Syntax")
        for i in range(len(sections)):
            if sections[i] == "": 
                continue
            if i % 2 == 0:
                split.append(TextNode(sections[i], TextType.PLAIN))
            else:
                split.append(TextNode(sections[i], text_type))
        new_nodes.extend(split)
    return new_nodes

def extract_markdown_images(text) ->tuple:
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)
# [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
def extract_markdown_links(text) -> tuple:
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)
# [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]

def split_nodes_image(old_nodes: list[TextNode])->list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        og_text = node.text
        images = extract_markdown_images(node.text)
        if len(images) == 0 and node.text != "": 
            new_nodes.append(node)
            continue
        for image in images:
            og_text = og_text.split(f"![{image[0]}]({image[1]})", 1)
            if og_text[0] != "":
                new_nodes.append(TextNode(og_text.pop(0), TextType.PLAIN))
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            og_text = "".join(og_text)
        if og_text != "":
            new_nodes.append(TextNode(og_text, TextType.PLAIN))
    return new_nodes

def split_nodes_link(old_nodes: list[TextNode])->list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        og_text = node.text
        images = extract_markdown_links(node.text)
        if len(images) == 0 and node.text != "": 
            new_nodes.append(node)
            continue
        for image in images:
            og_text = og_text.split(f"[{image[0]}]({image[1]})", 1)
            new_nodes.append(TextNode(og_text.pop(0), TextType.PLAIN))
            new_nodes.append(TextNode(image[0], TextType.LINK, image[1]))
            og_text = "".join(og_text)
        if og_text != "":
            new_nodes.append(TextNode(og_text, TextType.PLAIN))
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.PLAIN)]
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "**" ,TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_" ,TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`" ,TextType.CODE)
    return nodes