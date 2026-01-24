import unittest
from mbpp_563_code import extract_values

class TestExtractValues(unittest.TestCase):
    def test_typical_input(self):
        text = '"Hello", "World", "Python"'
        self.assertEqual(extract_values(text), ["Hello", "World", "Python"])

    def test_edge_case(self):
        text = '"Hello", "World"'
        self.assertEqual(extract_values(text), ["Hello", "World"])

    def test_edge_case_empty(self):
        text = ''
        self.assertEqual(extract_values(text), [])

    def test_edge_case_single(self):
        text = '"Hello"'
        self.assertEqual(extract_values(text), ["Hello"])

    def test_edge_case_multiple_spaces(self):
        text = '"Hello",   "World",   "Python"'
        self.assertEqual(extract_values(text), ["Hello", "World", "Python"])

    def test_edge_case_leading_trailing_spaces(self):
        text ='  "Hello",   "World",   "Python"   '
        self.assertEqual(extract_values(text), ["Hello", "World", "Python"])

    def test_invalid_input_non_string(self):
        text = 123
        with self.assertRaises(TypeError):
            extract_values(text)

    def test_invalid_input_non_string_list(self):
        text = [1, 2, 3]
        with self.assertRaises(TypeError):
            extract_values(text)
