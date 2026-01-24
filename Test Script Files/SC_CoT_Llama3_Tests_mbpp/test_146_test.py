import unittest
from mbpp_146_code import ascii_value_string

class TestAsciiValueString(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(ascii_value_string("Hello"), ord("H"))
        self.assertEqual(ascii_value_string("Hello"), ord("e"))
        self.assertEqual(ascii_value_string("Hello"), ord("l"))
        self.assertEqual(ascii_value_string("Hello"), ord("o"))

    def test_edge_case_empty_string(self):
        self.assertEqual(ascii_value_string(""), None)

    def test_edge_case_single_character(self):
        self.assertEqual(ascii_value_string("a"), ord("a"))

    def test_edge_case_empty_string_return(self):
        with self.assertRaises(TypeError):
            ascii_value_string()

    def test_edge_case_non_string_input(self):
        with self.assertRaises(TypeError):
            ascii_value_string(123)

    def test_edge_case_non_string_input_return(self):
        with self.assertRaises(TypeError):
            ascii_value_string(123)
