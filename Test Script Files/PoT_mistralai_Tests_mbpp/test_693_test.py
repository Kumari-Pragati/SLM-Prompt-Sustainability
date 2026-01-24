import unittest
from mbpp_693_code import remove_multiple_spaces

class TestRemoveMultipleSpaces(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(remove_multiple_spaces("hello   world"), "hello world")

    def test_edge_case_leading_trailing(self):
        self.assertEqual(remove_multiple_spaces("   hello world  "), "hello world")

    def test_edge_case_single_space(self):
        self.assertEqual(remove_multiple_spaces("hello world "), "hello world ")

    def test_edge_case_tab(self):
        self.assertEqual(remove_multiple_spaces("\thello\tworld"), "hello world")

    def test_corner_case_empty_string(self):
        self.assertEqual(remove_multiple_spaces(""), "")

    def test_corner_case_single_char(self):
        self.assertEqual(remove_multiple_spaces("a"), "a")
