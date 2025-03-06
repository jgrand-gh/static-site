import unittest

from block_markdown import markdown_to_blocks

class TestSplitNodesDelimiter(unittest.TestCase):

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

    
if __name__ == "__main__":
    unittest.main()