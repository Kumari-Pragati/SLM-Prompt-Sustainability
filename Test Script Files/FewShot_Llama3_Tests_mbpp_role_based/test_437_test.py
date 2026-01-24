import unittest
from mbpp_437_code import remove_odd

class TestRemoveOdd(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(remove_odd(""), "")

    def test_single_character(self):
        self.assertEqual(remove_odd("a"), "a")

    def test_even_length_string(self):
        self.assertEqual(remove_odd("abcdef"), "abcde")

    def test_odd_length_string(self):
        self.assertEqual(remove_odd("abcdefg"), "abcde")

    def test_string_with_multiple_odd_characters(self):
        self.assertEqual(remove_odd("abcdefgh"), "abcde")

    def test_string_with_multiple_even_characters(self):
        self.assertEqual(remove_odd("evenstring"), "evensting")

    def test_string_with_mixed_characters(self):
        self.assertEqual(remove_odd("aeiou"), "aeiou")
