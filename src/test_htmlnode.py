import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(props={
        "href": "https://www.google.com",
        "target": "_blank",
        })
        self.assertEqual(node.props_to_html()," href=\"https://www.google.com\" target=\"_blank\"")

    def test_noteqnodes(self):
        node = HTMLNode("p", "lorem ipsum", "huh", {"href":"uwu"} ) 
        node2 =  HTMLNode("p", "lorem ipsum", "huh", {"target":"uwu"} )
        self.assertNotEqual(node,node2)

    def test_tohtmlemtpy(self):
        node = HTMLNode("p", "lorem ipsum", "huh") 
        self.assertEqual(node.props_to_html(), "")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")   
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")



if __name__ == "__main__":
    unittest.main()