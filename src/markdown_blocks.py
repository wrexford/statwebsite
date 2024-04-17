from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node


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
    
    elif block.startswith("* "):  
        for line in text:
            if line.startswith("* ") == False:
                return block_type_paragraph 
        return block_type_unordered_list
    
    elif block.startswith("- "):  
        for line in text:
            if line.startswith("- ") == False:
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
    
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div",children,None)

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)

def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])

def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)

def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == block_type_paragraph:
        return paragraph_to_html_node(block)
    elif block_type == block_type_heading:
        return heading_to_html_node(block)
    elif block_type == block_type_code:
        return code_to_html_node(block)
    elif block_type == block_type_ordered_list:
        return olist_to_html_node(block)
    elif block_type == block_type_unordered_list:
        return ulist_to_html_node(block)
    elif block_type == block_type_quote:
        return quote_to_html_node(block)
    else:
        raise ValueError("Invalid block type")
    
