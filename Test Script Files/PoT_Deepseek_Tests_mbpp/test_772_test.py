import unittest
from mbpp_772_code import remove_length

class TestRemoveLength(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_length("Hello World", 5), "Hello World")

    def test_edge_case_empty_string(self):
        self.assertEqual(remove_length("", 5), "")

    def test_boundary_case_single_word(self):
        self.assertEqual(remove_length("Hello", 5), "")
        self.assertEqual(remove_length("Hello", 2), "Hello")

    def test_boundary_case_multiple_words_with_same_length(self):
        self.assertEqual(remove_length("Hello Hello", 5), "Hello Hello")
        self.assertEqual(remove_length("Hello Hello", 2), "")

    def test_corner_case_multiple_words_with_different_lengths(self):
        self.assertEqual(remove_length("Hello World", 5), "World")
        self.assertEqual(remove_length("Hello World", 2), "Hello")

    def test_invalid_input_negative_K(self):
        with self.assertRaises(Exception):
            remove_length("Hello World", -1)

    def test_invalid_input_non_string_test_str(self):
        with self.assertRaises(Exception):
            remove_length(12345, 2)
