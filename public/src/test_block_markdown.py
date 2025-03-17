import unittest

from block_markdown import BlockType, block_to_block_type, markdown_to_blocks

class TestBlockMarkdown(unittest.TestCase):

    # markdown_to_blocks tests
    def test_markdown_to_blocks(self):
        md = """
            This is **bolded** paragraph

            This is another paragraph with _italic_ text and `code` here
            This is the same paragraph on a new line

            - This is a list
            - with items
            """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    
    def test_markdown_to_blocks_single_block(self):
        md = """This is a single block of text."""
        blocks = markdown_to_blocks(md)
        assert blocks == ["This is a single block of text."]
    
    def test_markdown_to_blocks_multiple_blocks(self):
        md = """
        Block 1

        Block 2

        Block 3
        """
        blocks = markdown_to_blocks(md)
        assert blocks == ["Block 1", "Block 2", "Block 3"]

    def test_markdown_to_blocks_indented(self):
        md = """
            First block with spaces

            - Second block: a list
            - with leading spaces
        """
        blocks = markdown_to_blocks(md)
        assert blocks == [
            "First block with spaces",
            "- Second block: a list\n- with leading spaces",
        ]
    
    def test_markdown_to_blocks_excessive_blank_lines(self):
        md = """

        First block


        Second block



        Third block
        """
        blocks = markdown_to_blocks(md)
        assert blocks == ["First block", "Second block", "Third block"]

    def test_markdown_to_blocks_leading_trailing_newlines(self):
        md = """

        This is a block with some extra newline space  
        """
        blocks = markdown_to_blocks(md)
        assert blocks == ["This is a block with some extra newline space"]

    def test_markdown_to_blocks_empty_input(self):
        md = ""
        blocks = markdown_to_blocks(md)
        assert blocks == []    

    # tests for block_to_block_type
    def test_paragraph(self):
        block = "This is a simple paragraph with no special formatting."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_heading1(self):
        block = "# This is a header"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_heading2(self):
        block = "## This is a header"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_heading3(self):
        block = "### This is a header"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_heading4(self):
        block = "#### This is a header"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_heading5(self):
        block = "##### This is a header"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_heading6(self):
        block = "###### This is a header"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_invalid_heading(self):
        block = "####### This is a header"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_code(self):
        block = "```This is a code block```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_invalid_code(self):
        block = "``This is a code block```"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_code_multiline(self):
        block = "```This is a code block\nwith multiple lines\nof code```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_quote(self):
        block = ">To be, or not to be\n>That is the question"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_invalid_quote(self):
        block = "To be, or not to be\n>That is the question"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_unordered_list(self):
        block = "- Shopping\n- List\n- Unordered"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_invalid_unordered_list(self):
        block = "- Shopping\n2. List\n- Unordered"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_ordered_list(self):
        block = "1. Shopping\n2. List\n3. Ordered"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_invalid_ordered_list(self):
        block = "1. Shopping\n- List\n3. Ordered"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_invalid_out_of_ordered_list(self):
        block = "1. Shopping\n3. List\n2. Ordered"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    
if __name__ == "__main__":
    unittest.main()