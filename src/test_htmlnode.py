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
    
    def test_props_to_html(self):
        node = LEAFNode("a","Testing",None,{"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')






if __name__ == "__main__":
    unittest.main()

