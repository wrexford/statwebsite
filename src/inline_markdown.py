from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)

def split_nodes_delimiter(old_nodes,delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        new_string_list = old_node.text.split(delimiter) #split old_node into list(min 3, but odd since delimiter would break a string into 3 parts)
        if len(new_string_list) % 2 == 0:
            raise ValueError("Invalid markdown, not enough segments, delimiter not constructed")
        for i in range(0,len(new_string_list)):
            if new_string_list[i] == "":
                continue
            if i % 2 == 0: #since i starts at 0, the 2, 4 and etc repsent the 1st, 3rd, 5th, etc block of text and wouldnt have the "type"
                split_nodes.append(TextNode(new_string_list[i], text_type_text))
            else:
                split_nodes.append(TextNode(new_string_list[i],text_type))
        new_nodes.extend(split_nodes)
    return new_nodes