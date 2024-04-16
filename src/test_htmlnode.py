import unittest

from htmlnode import HTMLNode, LEAFNode, ParentNode

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
    
    def test_no_tag_to_html(self):
        node = LEAFNode(None,"Testing no tag")
        self.assertEqual(node.to_html(), 'Testing no tag')

class TestParentNode(unittest.TestCase):
    def test_to_html_nested(self):
        node = ParentNode(
            "p",
            [
                LEAFNode("b", "Bold text"),
                LEAFNode(None, "Normal text"),
                LEAFNode("i", "italic text"),
                LEAFNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )
        
    def test_to_html_with_child(self):
        test_child_node = LEAFNode("span", "test child")
        parent_node = ParentNode("div", [test_child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>test child</span></div>")

    def test_to_html_with_two_children(self):
        secondchild_node = LEAFNode("b", "second child")
        test_child_node = ParentNode("span", [secondchild_node])
        parent_node = ParentNode("div", [test_child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>second child</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()

