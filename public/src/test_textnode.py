import unittest

from textnode import TextNode, TextType
from htmlnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("This is NOT a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)        
    
    def test_not_eq_texttype(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    
    def test_url_none(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.url, None)
    
    def test_url_populated(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        self.assertEqual(node.url, "https://www.boot.dev")

    def test_repr(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(node.__repr__(), "TextNode(This is a text node, italic, None)")

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_textnode_to_leafnode_text(self):
        node = TextNode("words", TextType.TEXT)
        compare_node = LeafNode(None, "words")
        self.assertEqual(TextNode.text_node_to_html_node(node).to_html(), compare_node.to_html())
    
    def test_textnode_to_leafnode_bold(self):
        node = TextNode("words", TextType.BOLD)
        compare_node = LeafNode("b", "words")
        self.assertEqual(TextNode.text_node_to_html_node(node).to_html(), compare_node.to_html())

    def test_textnode_to_leafnode_italic(self):
        node = TextNode("words", TextType.ITALIC)
        compare_node = LeafNode("i", "words")
        self.assertEqual(TextNode.text_node_to_html_node(node).to_html(), compare_node.to_html())

    def test_textnode_to_leafnode_code(self):
        node = TextNode("words", TextType.CODE)
        compare_node = LeafNode("code", "words")
        self.assertEqual(TextNode.text_node_to_html_node(node).to_html(), compare_node.to_html())

    def test_textnode_to_leafnode_link(self):
        node = TextNode("DuckDuckGo", TextType.LINK, "http://www.duckduckgo.com")
        compare_node = LeafNode("a", "DuckDuckGo", {"href": "http://www.duckduckgo.com"})
        self.assertEqual(TextNode.text_node_to_html_node(node).to_html(), compare_node.to_html())

    def test_textnode_to_leafnode_image(self):
        node = TextNode("duck pic", TextType.IMAGE, "http://www.duckduckgo.com/duckpic")
        compare_node = LeafNode("img", "", {"src": "http://www.duckduckgo.com/duckpic", "alt": "duck pic"})
        self.assertEqual(TextNode.text_node_to_html_node(node).to_html(), compare_node.to_html())

    def test_textnode_leafnode_invalid_error(self):
        node = TextNode("words", "invalid")
        with self.assertRaises(Exception):
            TextNode.text_node_to_html_node(node).to_html()

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        compare_nodes = TextNode.split_nodes_delimiter([node], "`", TextType.CODE)
        expected_outcome = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT)
        ]
        self.assertEqual(compare_nodes, expected_outcome)

    def test_split_nodes_delimiter_multiple_delimiters(self):
        node = TextNode("This is `text` with a `code block` word", TextType.TEXT)
        compare_nodes = TextNode.split_nodes_delimiter([node], "`", TextType.CODE)
        expected_outcome = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.CODE),
            TextNode(" with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT)
        ]
        self.assertEqual(compare_nodes, expected_outcome)

    def test_split_nodes_delimiter_error(self):
        node = TextNode("This is text with a `code block word", TextType.TEXT)
        with self.assertRaises(ValueError):
            TextNode.split_nodes_delimiter([node], "`", TextType.CODE)

    # boot.dev suggested unit tests
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = TextNode.split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = TextNode.split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = TextNode.split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = TextNode.split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextType.TEXT)
        new_nodes = TextNode.split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = TextNode.split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = TextNode.split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main()