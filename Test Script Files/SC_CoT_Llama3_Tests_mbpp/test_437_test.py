import unittest
from mbpp_437_code import remove_odd

class TestRemoveOdd(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(remove_odd("hello"), "holo")

    def test_edge_case_empty_string(self):
        self.assertEqual(remove_odd(""), "")

    def test_edge_case_single_character(self):
        self.assertEqual(remove_odd("a"), "a")

    def test_edge_case_single_even_character(self):
        self.assertEqual(remove_odd("abc"), "bc")

    def test_edge_case_single_odd_character(self):
        self.assertEqual(remove_odd("abc"), "ac")

    def test_edge_case_multiple_even_characters(self):
        self.assertEqual(remove_odd("abcdef"), "bdf")

    def test_edge_case_multiple_odd_characters(self):
        self.assertEqual(remove_odd("abcdef"), "cf")

    def test_edge_case_all_even_characters(self):
        self.assertEqual(remove_odd("abcdef"), "abcdef")

    def test_edge_case_all_odd_characters(self):
        self.assertEqual(remove_odd("abcdef"), "")

    def test_edge_case_mixed_characters(self):
        self.assertEqual(remove_odd("abcdef"), "bdf")

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            remove_odd(123)

    def test_invalid_input_none(self):
        with self.assertRaises(TypeError):
            remove_odd(None)
