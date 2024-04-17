block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks
 
def block_to_block_type(block):
    text = block.split("\n")

    if len(block.lstrip("# ")) < len(block) and block.startswith("#"):
        return block_type_heading
    
    elif (text[0] == "```" and text[-1] == "```") and len(text) > 1:   
        return block_type_code
    
    elif block[0] == ">":   
        for line in text:
            if line.startswith(">") == False:
                return block_type_paragraph
        return block_type_quote
    
    elif block[0] == "* " or block[0] == "- ":  
        for line in text:
            if line.startswith("* ") == False and line.startwith("- ") == False:
                return block_type_paragraph 
        return block_type_unordered_list
    
    elif block[0].isdigit() == True and block[1] == "." and block[2]==" ":
        i=1
        for line in text:
            if line.startswith(f"{i}. "):
                return block_type_ordered_list
            else:          
                return block_type_paragraph
    else:
        return block_type_paragraph