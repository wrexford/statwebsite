from htmlnode import LEAFNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode:
    def __init__(self, text, text_type,url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, text2):
        return (
            self.text_type == text2.text_type
            and self.text == text2.text
            and self.url == text2.url
        )

    def __repr__(self):
         return str(f"TextNode({self.text}, {self.text_type}, {self.url})")

def text_node_to_html_node(text_node):
    if text_node.text_type == text_type_text:
        return LEAFNode(None, text_node.text)
    elif text_node.text_type == text_type_bold:
        return LEAFNode("b", text_node.text)
    elif text_node.text_type == text_type_italic:
        return LEAFNode("i", text_node.text)
    elif text_node.text_type == text_type_code:
        return LEAFNode("code", text_node.text)
    elif text_node.text_type == text_type_link:
        return LEAFNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == text_type_image:
        return LEAFNode("img", "", {"src": text_node.url, "alt":text_node.text})
    else:
        raise ValueError(f"Invalid text type: {text_node.text_type}")

