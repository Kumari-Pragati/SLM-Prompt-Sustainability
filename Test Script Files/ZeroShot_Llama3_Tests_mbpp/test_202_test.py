import unittest
from mbpp_202_code import remove_even

class TestRemoveEven(unittest.TestCase):

    def test_remove_even(self):
        self.assertEqual(remove_even("abcdef"), "bd")
        self.assertEqual(remove_even("123456"), "1357")
        self.assertEqual(remove_even("abcdefg"), "bdg")
        self.assertEqual(remove_even("1234567"), "1357")
        self.assertEqual(remove_even("123456789"), "13579")

    def test_remove_even_empty_string(self):
        self.assertEqual(remove_even(""), "")

    def test_remove_even_single_character(self):
        self.assertEqual(remove_even("a"), "a")

    def test_remove_even_no_even_characters(self):
        self.assertEqual(remove_even("odd"), "odd")

    def test_remove_even_all_even_characters(self):
        self.assertEqual(remove_even("even"), "")
