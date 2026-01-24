import unittest
from mbpp_450_code import extract_string

class TestExtractString(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(extract_string("hello world", 2), ["he", "ll", "o ", "wo", "rl", "rd"])

    def test_edge_case_empty_string(self):
        self.assertEqual(extract_string("", 2), [])

    def test_edge_case_single_char_string(self):
        self.assertEqual(extract_string("a", 1), ["a"])

    def test_edge_case_single_char_string_with_spaces(self):
        self.assertEqual(extract_string("a b", 1), ["a", "b"])

    def test_edge_case_empty_string_with_spaces(self):
        self.assertEqual(extract_string("   ", 1), [])

    def test_edge_case_invalid_input_type(self):
        with self.assertRaises(TypeError):
            extract_string(123, 2)

    def test_edge_case_invalid_input_type2(self):
        with self.assertRaises(TypeError):
            extract_string("hello", 'a')

    def test_edge_case_invalid_input_type3(self):
        with self.assertRaises(TypeError):
            extract_string(None, 2)

    def test_edge_case_invalid_input_type4(self):
        with self.assertRaises(TypeError):
            extract_string("hello", None)
