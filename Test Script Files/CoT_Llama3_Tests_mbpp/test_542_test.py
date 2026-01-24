import unittest
from mbpp_542_code import fill_spaces

class TestFillSpaces(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(fill_spaces("Hello, world!"), "Hello:, world:")

    def test_edge_case_empty_string(self):
        self.assertEqual(fill_spaces(""), "")

    def test_edge_case_single_space(self):
        self.assertEqual(fill_spaces(" "), ":")

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(fill_spaces("   "), ":")

    def test_edge_case_comma(self):
        self.assertEqual(fill_spaces("Hello, world!"), "Hello:, world:")

    def test_edge_case_period(self):
        self.assertEqual(fill_spaces("Hello. world!"), "Hello.: world:")

    def test_edge_case_multiple_characters(self):
        self.assertEqual(fill_spaces("Hello, world!"), "Hello:, world:")

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            fill_spaces(123)
