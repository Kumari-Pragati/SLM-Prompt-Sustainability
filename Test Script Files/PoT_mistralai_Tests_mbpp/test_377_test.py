import unittest
from mbpp_377_code import remove_Char

class TestRemoveChar(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_Char('', 'a'), '')

    def test_single_char_string(self):
        self.assertEqual(remove_Char('a', 'a'), '')
        self.assertEqual(remove_Char('A', 'a'), 'A')

    def test_multiple_chars_string(self):
        self.assertEqual(remove_Char('aa', 'a'), '')
        self.assertEqual(remove_Char('AA', 'a'), '')
        self.assertEqual(remove_Char('aaA', 'a'), 'A')
        self.assertEqual(remove_Char('AaA', 'a'), 'A')

    def test_single_char_in_middle(self):
        self.assertEqual(remove_Char('abc', 'b'), 'ac')
        self.assertEqual(remove_Char('ABC', 'b'), 'AC')

    def test_single_char_at_start(self):
        self.assertEqual(remove_Char('abc', 'a'), 'bc')
        self.assertEqual(remove_Char('ABC', 'A'), 'BC')

    def test_single_char_at_end(self):
        self.assertEqual(remove_Char('abc', 'c'), 'ab')
        self.assertEqual(remove_Char('ABC', 'C'), 'AB')

    def test_multiple_chars_in_middle(self):
        self.assertEqual(remove_Char('abcba', 'b'), 'ac')
        self.assertEqual(remove_Char('ABCBA', 'B'), 'AC')

    def test_multiple_chars_at_start(self):
        self.assertEqual(remove_Char('bbabc', 'b'), 'ac')
        self.assertEqual(remove_Char('BBABC', 'B'), 'AC')

    def test_multiple_chars_at_end(self):
        self.assertEqual(remove_Char('abcbb', 'b'), 'ac')
        self.assertEqual(remove_Char('ABCBB', 'B'), 'AC')
