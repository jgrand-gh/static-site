import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("p", "This is sample paragraph text", None, {"href": "https://www.google.com", "target": "_blank",})
        expected_text_string = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_text_string)
    
    def test_props_to_html2(self):
        node = HTMLNode("p", "This is sample paragraph text", None, {"href": "https://www.google.com", "target": "_blank", "img": "none", "alt": "alt-text"})
        expected_text_string = ' href="https://www.google.com" target="_blank" img="none" alt="alt-text"'
        self.assertEqual(node.props_to_html(), expected_text_string)

    def test_props_to_html_none(self):
        node = HTMLNode()
        expected_text_string = ""
        self.assertEqual(node.props_to_html(), expected_text_string)
    
    def test_props_to_html_empty_dict(self):
        node = HTMLNode(None, None, None, {})
        expected_text_string = ""
        self.assertEqual(node.props_to_html(), expected_text_string)        

    def test_repr(self):
        node = HTMLNode("p", "text", None, {"class": "para"})
        expected = 'HTMLNode(p, text, children: None, {\'class\': \'para\'})'
        self.assertEqual(node.__repr__(), expected)

    def test_repr_none(self):
        node = HTMLNode()
        expected = 'HTMLNode(None, None, children: None, None)'
        self.assertEqual(node.__repr__(), expected)
    
    def test_none_tag(self):
        node = HTMLNode()
        self.assertEqual(node.tag, None)

    def test_none_value(self):
        node = HTMLNode()
        self.assertEqual(node.value, None)

    def test_none_children(self):
        node = HTMLNode()
        self.assertEqual(node.children, None)

    def test_none_props(self):
        node = HTMLNode()
        self.assertEqual(node.props, None)

    def test_to_html(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_empty_leaf_node(self):
        with self.assertRaises(TypeError):
            node = LeafNode()
    
    def test_none_leaf_node(self):
        with self.assertRaises(ValueError):
            node = LeafNode(None, None).to_html()

    def test_leaf_node_to_html(self):
        node = LeafNode("p", "This is a line of text")
        expected_string_output = "<p>This is a line of text</p>"
        self.assertEqual(node.to_html(), expected_string_output)

    def test_leaf_note_to_html_no_tag(self):
        node = LeafNode(None, "This is a line of text")
        expected_string_output = "This is a line of text"
        self.assertEqual(node.to_html(), expected_string_output)

    #boot.dev suggested tests:
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

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )

if __name__ == "__main__":
    unittest.main()