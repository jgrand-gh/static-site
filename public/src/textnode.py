from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
    def text_node_to_html_node(text_node):
        match (text_node.text_type):
            case TextType.TEXT:
                return LeafNode(None, text_node.text)
            case TextType.BOLD:
                return LeafNode("b", text_node.text)
            case TextType.ITALIC:
                return LeafNode("i", text_node.text)
            case TextType.CODE:
                return LeafNode("code", text_node.text)
            case TextType.LINK:
                return LeafNode("a", text_node.text, {"href": text_node.url})
            case TextType.IMAGE:
                return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
            case _:
                raise Exception("text node has no specified TextType")
    
    def split_nodes_delimiter(old_nodes, delimiter, text_type):
        new_nodes = []

        for node in old_nodes:
            if node.text_type != TextType.TEXT:
                new_nodes.append(node)
            else:
                if delimiter in node.text:
                    split_nodes = node.text.split(delimiter)

                    if len(split_nodes) % 2 == 0:
                        raise ValueError(f"Invalid markdown: Unclosed delimiter {delimiter}")

                    for i in range(len(split_nodes)):
                        if split_nodes[i] == "":
                            continue
                        if i % 2 == 0:
                            new_nodes.append(TextNode(split_nodes[i], TextType.TEXT))
                        else:
                            new_nodes.append(TextNode(split_nodes[i], text_type))
                else:
                    new_nodes.append(node)

        return new_nodes
