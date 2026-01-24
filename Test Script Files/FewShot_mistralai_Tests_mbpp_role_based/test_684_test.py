import unittest
from mbpp_684_code import count_Char

class TestCountChar(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(count_Char('', 'a'), 0)

    def test_single_character(self):
        self.assertEqual(count_Char('a', 'a'), 1)

    def test_multiple_characters(self):
        self.assertEqual(count_Char('abc', 'a'), 3)

    def test_long_string(self):
        long_string = 'x' * 100
        self.assertEqual(count_Char(long_string, 'x'), 100)

    def test_string_with_multiple_characters(self):
        self.assertEqual(count_Char('abab', 'a'), 4)

    def test_string_with_repeated_characters(self):
        self.assertEqual(count_Char('aaaaa', 'a'), 5)

    def test_string_with_no_matching_characters(self):
        self.assertEqual(count_Char('abc', 'd'), 0)

    def test_string_with_short_repetitions(self):
        self.assertEqual(count_Char('aaa', 'a'), 3)

    def test_string_with_long_repetitions(self):
        long_string = 'x' * 100
        self.assertEqual(count_Char(long_string, 'x'), 100)
