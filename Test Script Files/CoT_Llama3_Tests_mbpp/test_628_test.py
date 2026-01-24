import unittest
from mbpp_628_code import replace_spaces

class TestReplaceSpaces(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(replace_spaces("Hello World"), "0%20World%20Hello")
        self.assertEqual(replace_spaces("   Hello   World   "), "0%20Hello%20World")
        self.assertEqual(replace_spaces("Hello"), "Hello")

    def test_max_length_exceeded(self):
        self.assertEqual(replace_spaces("a"*1001), -1)

    def test_no_spaces(self):
        self.assertEqual(replace_spaces("Hello"), "Hello")

    def test_single_space(self):
        self.assertEqual(replace_spaces("Hello World"), "0%20World%20Hello")

    def test_multiple_spaces(self):
        self.assertEqual(replace_spaces("Hello   World   "), "0%20World%20Hello")

    def test_edge_cases(self):
        self.assertEqual(replace_spaces(""), "")
        self.assertEqual(replace_spaces(" "), "0%20")
