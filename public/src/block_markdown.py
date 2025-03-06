import textwrap

def markdown_to_blocks(markdown):
    markdown = textwrap.dedent(markdown)
    markdown_nodes = markdown.split("\n\n")

    filtered_list = []
    for node in markdown_nodes:
        if node == "":
            continue
        node = node.strip()
        filtered_list.append(node)

    return filtered_list