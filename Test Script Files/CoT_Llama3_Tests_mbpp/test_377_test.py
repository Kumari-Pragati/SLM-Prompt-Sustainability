import unittest
from mbpp_377_code import remove_Char

class TestRemoveChar(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(remove_Char("hello world", "o"), "hell wrld")

    def test_edge_case_empty_string(self):
        self.assertEqual(remove_Char("", "a"), "")

    def test_edge_case_empty_string_and_char(self):
        self.assertEqual(remove_Char("", "a"), "")

    def test_edge_case_no_char_in_string(self):
        self.assertEqual(remove_Char("hello world", "z"), "hello world")

    def test_edge_case_no_char_in_string_and_empty_string(self):
        self.assertEqual(remove_Char("", "z"), "")

    def test_edge_case_multiple_chars(self):
        self.assertEqual(remove_Char("hello world", "o"), "hell wrld")

    def test_edge_case_multiple_chars_and_empty_string(self):
        self.assertEqual(remove_Char("", "o"), "")

    def test_edge_case_multiple_chars_and_no_char_in_string(self):
        self.assertEqual(remove_Char("hello world", "o"), "hello world")

    def test_edge_case_multiple_chars_and_no_char_in_string_and_empty_string(self):
        self.assertEqual(remove_Char("", "o"), "")

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            remove_Char(123, "a")

    def test_invalid_input_non_string_and_char(self):
        with self.assertRaises(TypeError):
            remove_Char(123, "a")

    def test_invalid_input_non_string_and_empty_string(self):
        with self.assertRaises(TypeError):
            remove_Char(123, "")

    def test_invalid_input_non_string_and_empty_string_and_char(self):
        with self.assertRaises(TypeError):
            remove_Char(123, "")
