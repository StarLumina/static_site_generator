from textnode import *
import os
import shutil
import re
from markdown_to_htmlnode import markdown_to_html_node

def main():
    print("Running main...\n wait a sec bbgrl")
    toSmithereens()
    copy_static()

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
    if re.match(r"# ",markdown):
        raise Exception("No title found")
    return markdown.split("# ")[-1]("\n")[0]

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    fromFile = from_path.read()
    templateFile = template_path.read()
    html = markdown_to_html_node(fromFile)
    

main()

