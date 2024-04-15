import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", text_type_text,"https://www.boot.dev")
        node2 = TextNode("This is a text node", text_type_text,"https://www.boot.dev")
        self.assertEqual(node, node2)
    
    def test_eq_url_none(self):
        node = TextNode("This is a text node", text_type_bold,None)
        node2 = TextNode("This is a text node", text_type_bold,None)
        self.assertEqual(node, node2)
          
    def test_eq_falsetext(self):
        node = TextNode("This is text node 1", text_type_italic)
        node2 = TextNode("This is text node 2", text_type_italic)
        self.assertNotEqual(node, node2)

    def test_eq_falsetext_type(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", text_type_bold, "https://www.boot.dev")
        self.assertEqual("TextNode(This is a text node, bold, https://www.boot.dev)", repr(node))        


if __name__ == "__main__":
    unittest.main()
