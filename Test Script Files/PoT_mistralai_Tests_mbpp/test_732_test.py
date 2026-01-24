import unittest
from mbpp_732_code import replace_specialchar

class TestReplaceSpecialchar(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(replace_specialchar("Hello, World.!"), "Hello:World:!")

    def test_edge_case_empty_string(self):
        self.assertEqual(replace_specialchar(""), "")

    def test_edge_case_single_char(self):
        self.assertEqual(replace_specialchar("a"), "a")

    def test_edge_case_single_special_char(self):
        self.assertEqual(replace_specialchar(","), ":")
        self.assertEqual(replace_specialchar("."), ":")

    def test_edge_case_single_space(self):
        self.assertEqual(replace_specialchar(" "), ":")

    def test_corner_case_multiple_spaces(self):
        self.assertEqual(replace_specialchar("  Hello, World.!  "), "  Hello:World:!  ")

    def test_corner_case_multiple_special_chars(self):
        self.assertEqual(replace_specialchar("Hello,,World.!,,"), "Hello:World:!:")
