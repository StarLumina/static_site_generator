def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    new_blocks = []
    for block in blocks:
        if block.strip() != "":
            new_blocks.append(block.strip())    
    return new_blocks