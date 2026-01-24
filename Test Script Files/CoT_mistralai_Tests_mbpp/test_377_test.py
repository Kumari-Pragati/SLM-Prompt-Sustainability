import unittest
from mbpp_377_code import remove_Char

class TestRemoveChar(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(remove_Char('', 'a'), '')

    def test_single_char_string(self):
        self.assertEqual(remove_Char('a', 'a'), '')
        self.assertEqual(remove_Char('A', 'a'), '')

    def test_multiple_chars_string(self):
        self.assertEqual(remove_Char('aa', 'a'), '')
        self.assertEqual(remove_Char('AA', 'a'), '')
        self.assertEqual(remove_Char('ab', 'a'), 'b')
        self.assertEqual(remove_Char('AB', 'a'), 'B')
        self.assertEqual(remove_Char('abc', 'a'), 'bc')
        self.assertEqual(remove_Char('ABC', 'a'), 'BC')

    def test_single_char_in_middle(self):
        self.assertEqual(remove_Char('abc', 'b'), 'aac')
        self.assertEqual(remove_Char('ABC', 'B'), 'AaC')

    def test_multiple_chars_in_middle(self):
        self.assertEqual(remove_Char('abcd', 'b'), 'acd')
        self.assertEqual(remove_Char('ABCD', 'B'), 'ACD')
        self.assertEqual(remove_Char('abcde', 'b'), 'acde')
        self.assertEqual(remove_Char('ABCDE', 'B'), 'ACDE')

    def test_single_char_at_start(self):
        self.assertEqual(remove_Char('abc', 'a'), 'bc')
        self.assertEqual(remove_Char('ABC', 'A'), 'BC')

    def test_single_char_at_end(self):
        self.assertEqual(remove_Char('abc', 'c'), 'ab')
        self.assertEqual(remove_Char('ABC', 'C'), 'AB')

    def test_multiple_chars_at_start(self):
        self.assertEqual(remove_Char('abc', 'ab'), 'c')
        self.assertEqual(remove_Char('ABC', 'AB'), '')

    def test_multiple_chars_at_end(self):
        self.assertEqual(remove_Char('abc', 'c'), 'ab')
        self.assertEqual(remove_Char('ABC', 'C'), 'AB')

    def test_multiple_chars_in_start_and_end(self):
        self.assertEqual(remove_Char('abc', 'ac'), 'b')
        self.assertEqual(remove_Char('ABC', 'CA',), 'B')

    def test_multiple_chars_in_start_and_middle(self):
        self.assertEqual(remove_Char('abc', 'ab'), 'c')
        self.assertEqual(remove_Char('ABC', 'AB'), '')

    def test_multiple_chars_in_middle_and_end(self):
        self.assertEqual(remove_Char('abc', 'bc'), 'a')
        self.assertEqual(remove_Char('ABC', 'BC'), 'A')

    def test_empty_list_removal(self):
        self.assertEqual(remove_Char('', 'a'), '')

    def test_single_char_list_removal(self):
        self.assertEqual(remove_Char(['a'], 'a'), [])
        self.assertEqual(remove_Char(['A'], 'a'), [])

    def test_multiple_chars_list_removal(self):
        self.assertEqual(remove_Char(['a', 'a'], 'a'), [])
        self.assertEqual(remove_Char(['A', 'A'], 'a'), [])
        self.assertEqual(remove_Char(['a', 'b'], 'a'), ['b'])
        self.assertEqual(remove_Char(['A', 'B'], 'a'), ['B'])
        self.assertEqual(remove_Char(['a', 'b', 'c'], 'a'), ['b', 'c'])
        self.assertEqual(remove_Char(['A', 'B', 'C'], 'a'), ['B', 'C'])
