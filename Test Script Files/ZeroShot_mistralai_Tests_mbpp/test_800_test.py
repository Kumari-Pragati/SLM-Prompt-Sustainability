import unittest
from mbpp_800_code import remove_all_spaces

class TestRemoveAllSpaces(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_all_spaces(''), '')

    def test_single_space(self):
        self.assertEqual(remove_all_spaces(' '), '')

    def test_multiple_spaces(self):
        self.assertEqual(remove_all_spaces('   '), '')

    def test_leading_trailing_spaces(self):
        self.assertEqual(remove_all_spaces(' a b   c   '), 'a b c')

    def test_spaces_in_middle(self):
        self.assertEqual(remove_all_spaces('a b c d   e   f g'), 'a b c d e f g')

    def test_spaces_at_beginning_and_end(self):
        self.assertEqual(remove_all_spaces('   a   b   '), 'a b')

    def test_spaces_only(self):
        self.assertEqual(remove_all_spaces('   \t\n\r  '), '')

    def test_special_characters_and_spaces(self):
        self.assertEqual(remove_all_spaces('a b c \t d e f \n g h i \r j k l'), 'a b c d e f g h i j k l')
