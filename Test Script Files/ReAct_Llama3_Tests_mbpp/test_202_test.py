import unittest
from mbpp_202_code import remove_even

class TestRemoveEven(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(remove_even("abcdef"), "bd")

    def test_edge_case_empty_string(self):
        self.assertEqual(remove_even(""), "")

    def test_edge_case_single_character(self):
        self.assertEqual(remove_even("a"), "a")

    def test_edge_case_even_length_string(self):
        self.assertEqual(remove_even("abcdefgh"), "bdfh")

    def test_edge_case_odd_length_string(self):
        self.assertEqual(remove_even("abcdefg"), "bdfg")

    def test_edge_case_long_string(self):
        self.assertEqual(remove_even("abcdefghijklmnopqrstuvwxyz"), "bdfghjklmpqrstuvwxzy")

    def test_edge_case_non_string_input(self):
        with self.assertRaises(TypeError):
            remove_even(123)
