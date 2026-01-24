import unittest
from mbpp_202_code import remove_even

class TestRemoveEven(unittest.TestCase):
    def test_remove_even_from_empty_string(self):
        self.assertEqual(remove_even(""), "")

    def test_remove_even_from_single_character_string(self):
        self.assertEqual(remove_even("a"), "a")

    def test_remove_even_from_even_length_string(self):
        self.assertEqual(remove_even("abcdef"), "cadf")

    def test_remove_even_from_odd_length_string(self):
        self.assertEqual(remove_even("abcdefg"), "cadfg")

    def test_remove_even_from_string_with_multiple_even_length_substrings(self):
        self.assertEqual(remove_even("abcdefabcdef"), "cadfcaf")

    def test_remove_even_from_string_with_multiple_odd_length_substrings(self):
        self.assertEqual(remove_even("abcdefabcdefg"), "cadfgcaf")
