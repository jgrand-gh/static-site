import unittest
from blocktype import BlockType, block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    
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
