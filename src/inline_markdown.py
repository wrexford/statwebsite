import re

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image
)

def text_to_textnodes(text):
    nodes = [TextNode(text, text_type_text)]
    nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
    nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes


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

def extract_markdown_images(text):
    result=re.findall(r"!\[(.*?)\]\((.*?)\)",text)
    #print(f'Regex link result {result}')   
    return result

def extract_markdown_links(text):
    result=re.findall(r"\[(.*?)\]\((.*?)\)",text)
    #print(f'Regex link result {result}')
    return result

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes: 
            if old_node.text_type != text_type_text: #if it isnt a string, do not work on it
                new_nodes.append(old_node)
                continue
            old_text = old_node.text #pull text string from old node
            images = extract_markdown_images(old_text) #return list of tuples of all images in string
            if len(images) == 0: #if we found no images in string, append string and move to next
                new_nodes.append(old_node)
                continue
            for image in images: #if we found images, iterate through tuple list
                new_image_list = old_text.split(f"![{image[0]}]({image[1]})", 1)  #split where string matches the regex search result
                #print(new_image_list)
                if len(new_image_list) != 2: 
                    raise ValueError("Invalid markdown, image section not closed")
                if new_image_list[0] != "": #if first half of string isnt blank append text from split
                    new_nodes.append(TextNode(new_image_list[0], text_type_text))
                #then append the extracted image and path with known image type
                new_nodes.append(
                    TextNode(
                        image[0],
                        text_type_image,
                        image[1],
                    )
                )
                old_text = new_image_list[1] #update the old_text to contain the backhalf of the split string for loop
            if old_text != "": #after exiting loop, if last loop still contained text append it
                new_nodes.append(TextNode(old_text, text_type_text))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes: 
            if old_node.text_type != text_type_text: #if it isnt a string, do not work on it
                new_nodes.append(old_node)
                continue
            old_text = old_node.text #pull text string from old node
            links = extract_markdown_links(old_text) #return list of tuples of all links in string
            if len(links) == 0: #if we found no links in string, append string and move to next
                new_nodes.append(old_node)
                continue
            for link in links: #if we found links, iterate through tuple list
                new_link_list = old_text.split(f"[{link[0]}]({link[1]})", 1)  #split where string matches the regex search result
                if len(new_link_list) != 2: 
                    raise ValueError("Invalid markdown, link section not closed")
                if new_link_list[0] != "": #if first half of string isnt blank append text from split
                    new_nodes.append(TextNode(new_link_list[0], text_type_text))
                #then append the extracted link and path with known link type
                new_nodes.append(
                    TextNode(
                        link[0],
                        text_type_link,
                        link[1],
                    )
                )
                old_text = new_link_list[1] #update the old_text to contain the backhalf of the split string for loop
            if old_text != "": #after exiting loop, if last loop still contained text append it
                new_nodes.append(TextNode(old_text, text_type_text))
    return new_nodes