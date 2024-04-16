import unittest

from htmlnode import HTMLNode, LEAFNode

class TestHTMLNode(unittest.TestCase):
    
    def test_props_to_html(self):
        node = HTMLNode("a","Testing",None,{"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_repr(self):
        node = HTMLNode(None,None,None,{"href": "https://www.google.com", "target": "_blank"})
        #print(node)

class TestLEAFNode(unittest.TestCase):
    
    def test_tag_a_to_html(self):
        node = LEAFNode("a","Testing",{"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com" target="_blank">Testing</a>')

    def test_tag_p_to_html(self):
        node = LEAFNode("p","Testing p tag")
        self.assertEqual(node.to_html(), '<p>Testing p tag</p>')



if __name__ == "__main__":
    unittest.main()

