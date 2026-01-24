import unittest
from mbpp_732_code import replace_specialchar

class TestReplaceSpecialchar(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(replace_specialchar("Hello, world!"), "Hello:, world:")

    def test_edge_case_empty_string(self):
        self.assertEqual(replace_specialchar(""), "")

    def test_edge_case_single_space(self):
        self.assertEqual(replace_specialchar(" "), ":")

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(replace_specialchar("   "), ":")

    def test_edge_case_comma(self):
        self.assertEqual(replace_specialchar("Hello, world!"), "Hello:, world:")

    def test_edge_case_period(self):
        self.assertEqual(replace_specialchar("Hello. world!"), "Hello.: world:")

    def test_edge_case_multiple_characters(self):
        self.assertEqual(replace_specialchar("Hello, world. This is a test!"), "Hello:, world.: This : is : a : test:")

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            replace_specialchar(123)

    def test_invalid_input_none(self):
        with self.assertRaises(TypeError):
            replace_specialchar(None)
