import unittest
from mbpp_437_code import remove_odd

class TestRemoveOdd(unittest.TestCase):

    def test_even_length_string(self):
        self.assertEqual(remove_odd("abcdef"), "abcde")

    def test_odd_length_string(self):
        self.assertEqual(remove_odd("abcdefg"), "abcde")

    def test_single_character_string(self):
        self.assertEqual(remove_odd("a"), "")

    def test_empty_string(self):
        self.assertEqual(remove_odd(""), "")

    def test_no_change(self):
        self.assertEqual(remove_odd("abc"), "abc")

    def test_all_odd(self):
        self.assertEqual(remove_odd("abcdefg"), "")

    def test_all_even(self):
        self.assertEqual(remove_odd("abcde"), "abcde")
