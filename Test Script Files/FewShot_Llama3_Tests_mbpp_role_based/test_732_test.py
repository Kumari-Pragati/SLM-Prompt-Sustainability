import unittest
from mbpp_732_code import replace_specialchar

class TestReplaceSpecialchar(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(replace_specialchar("Hello, World!"), "Hello:, World:")

    def test_edge_case_empty_string(self):
        self.assertEqual(replace_specialchar(""), "")

    def test_edge_case_single_space(self):
        self.assertEqual(replace_specialchar(" "), ":")

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(replace_specialchar("   "), ":")

    def test_edge_case_comma(self):
        self.assertEqual(replace_specialchar("Hello, World!"), "Hello:, World:")

    def test_edge_case_period(self):
        self.assertEqual(replace_specialchar("Hello. World!"), "Hello.: World:")

    def test_edge_case_multiple_special_chars(self):
        self.assertEqual(replace_specialchar("Hello, World. This is a test!"), "Hello:, World.: This is a test:")
