import unittest
from mbpp_437_code import remove_odd

class TestRemoveOdd(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(remove_odd("hello"), "holo")

    def test_edge_case_empty_string(self):
        self.assertEqual(remove_odd(""), "")

    def test_edge_case_single_character(self):
        self.assertEqual(remove_odd("a"), "a")

    def test_edge_case_even_length_string(self):
        self.assertEqual(remove_odd("abcdef"), "abcde")

    def test_edge_case_odd_length_string(self):
        self.assertEqual(remove_odd("abcdefg"), "abcde")

    def test_edge_case_long_string(self):
        self.assertEqual(remove_odd("abcdefghijklmnopqrstuvwxyz"), "abcde")

    def test_edge_case_all_odd_characters(self):
        self.assertEqual(remove_odd("13579"), "")

    def test_edge_case_all_even_characters(self):
        self.assertEqual(remove_odd("24680"), "24680")

    def test_edge_case_mixed_characters(self):
        self.assertEqual(remove_odd("1357924680"), "24680")
