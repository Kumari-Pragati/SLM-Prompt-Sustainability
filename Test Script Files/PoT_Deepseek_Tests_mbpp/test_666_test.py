import unittest
from mbpp_666_code import count_char

class TestCountChar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_char('hello', 'l'), 2)

    def test_edge_case_empty_string(self):
        self.assertEqual(count_char('', 'a'), 0)

    def test_boundary_case_single_char(self):
        self.assertEqual(count_char('a', 'a'), 1)
        self.assertEqual(count_char('a', 'b'), 0)

    def test_corner_case_repeated_char(self):
        self.assertEqual(count_char('aaaaa', 'a'), 5)

    def test_corner_case_case_insensitive(self):
        self.assertEqual(count_char('Hello', 'h'), 1)

    def test_corner_case_special_characters(self):
        self.assertEqual(count_char('hello world!', 'o'), 2)

    def test_corner_case_whitespace(self):
        self.assertEqual(count_char('hello world', ' '), 1)
