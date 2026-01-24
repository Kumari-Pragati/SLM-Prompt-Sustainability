import unittest
from mbpp_693_code import remove_multiple_spaces

class TestRemoveMultipleSpaces(unittest.TestCase):
    def test_simple_single_space(self):
        self.assertEqual(remove_multiple_spaces('a b'), 'a b')

    def test_simple_multiple_spaces(self):
        self.assertEqual(remove_multiple_spaces('a   b   c'), 'a b c')

    def test_simple_leading_trailing_spaces(self):
        self.assertEqual(remove_multiple_spaces('   a   '), 'a')
        self.assertEqual(remove_multiple_spaces('a   '), 'a')
        self.assertEqual(remove_multiple_spaces('  a'), 'a')

    def test_edge_empty_string(self):
        self.assertEqual(remove_multiple_spaces(''), '')

    def test_edge_single_word(self):
        self.assertEqual(remove_multiple_spaces('a'), 'a')

    def test_edge_single_space_at_start_and_end(self):
        self.assertEqual(remove_multiple_spaces(' a b '), 'a b')

    def test_edge_multiple_spaces_at_start_and_end(self):
        self.assertEqual(remove_multiple_spaces('   a   b   '), 'a b')

    def test_edge_multiple_spaces_in_middle(self):
        self.assertEqual(remove_multiple_spaces('a   b   c   '), 'a b c')

    def test_edge_multiple_spaces_at_start_and_end_with_single_space(self):
        self.assertEqual(remove_multiple_spaces(' a  b  '), 'a b')
