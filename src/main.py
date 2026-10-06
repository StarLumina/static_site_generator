from textnode import *
import os
import shutil
import re
from markdown_to_htmlnode import markdown_to_html_node

def main():
    print("Running main...\n wait a sec bbgrl")
    toSmithereens()
    copy_static()
    generate_page("content/index.md", "template.html", "public/index.html")

def copy_static (copyTo: str = "public", copyFrom: str = "static"):
    list_to_copy = os.listdir(copyFrom)
    for item in list_to_copy:
        pathOfItem = os.path.join(copyFrom,item)
        if os.path.isfile(pathOfItem):
            shutil.copy(pathOfItem, copyTo)
            print(f"copying {pathOfItem} to {copyTo}")
        else:
            newAddress = os.path.join(copyTo,item)
            os.mkdir(newAddress)
            copy_static(newAddress, os.path.join(copyFrom, item))
    #helper function to delete, posibly use same one to clear first
    return

def toSmithereens():
    shutil.rmtree(os.path.abspath("./public"))
    os.mkdir(os.path.abspath("./public"))

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("No title found")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as file:
        with open(template_path) as template:
            fileText = file.read()
            templateFile = template.read()
            html = markdown_to_html_node(fileText).to_html()
            title = extract_title(fileText)
            htmlFile = templateFile.replace("{{ Title }}", title).replace("{{ Content }}", html)
            dest = os.path.dirname(dest_path)
            os.makedirs(dest, exist_ok = True)
            with open(dest_path, "w") as destination:
                destination.write(htmlFile)
    


main()

