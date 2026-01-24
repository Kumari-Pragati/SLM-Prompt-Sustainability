import unittest
from mbpp_437_code import remove_odd

class TestRemoveOdd(unittest.TestCase):

    def test_remove_odd(self):
        self.assertEqual(remove_odd("Hello"), "Hlo")
        self.assertEqual(remove_odd("Python"), "Pto")
        self.assertEqual(remove_odd("Unittest"), "Unitt")
        self.assertEqual(remove_odd("123456"), "246")
        self.assertEqual(remove_odd("abcdef"), "acef")
        self.assertEqual(remove_odd(""), "")
        self.assertEqual(remove_odd("a"), "a")
        self.assertEqual(remove_odd("abc"), "bc")

    def test_remove_odd_empty_string(self):
        self.assertEqual(remove_odd(""), "")

    def test_remove_odd_single_character(self):
        self.assertEqual(remove_odd("a"), "a")

    def test_remove_odd_single_character_odd(self):
        self.assertEqual(remove_odd("b"), "")

    def test_remove_odd_single_character_even(self):
        self.assertEqual(remove_odd("a"), "a")

    def test_remove_odd_multiple_characters(self):
        self.assertEqual(remove_odd("abc"), "bc")

    def test_remove_odd_multiple_characters_odd(self):
        self.assertEqual(remove_odd("abcd"), "cd")

    def test_remove_odd_multiple_characters_even(self):
        self.assertEqual(remove_odd("abcde"), "ace")
