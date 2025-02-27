import re

from textnode import TextNode, TextType

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

def extract_markdown_images(text):
    regex_pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(regex_pattern, text)
    return matches

def extract_markdown_links(text):
    regex_pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(regex_pattern, text)
    return matches