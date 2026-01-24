import unittest
from mbpp_546_code import last_occurence_char

class TestLastOccurenceChar(unittest.TestCase):
    def test_empty_string(self):
        self.assertIsNone(last_occurence_char('', 'a'))

    def test_single_char_string(self):
        self.assertEqual(last_occurence_char('a', 'a'), 1)

    def test_multiple_chars_string(self):
        self.assertEqual(last_occurence_char('abc', 'c'), 3)

    def test_multiple_chars_different_char(self):
        self.assertIsNone(last_occurence_char('abc', 'd'))

    def test_char_at_beginning(self):
        self.assertEqual(last_occurence_char('abc', 'a'), 3)

    def test_char_at_end(self):
        self.assertEqual(last_occurence_char('abc', 'c'), 3)

    def test_char_in_middle(self):
        self.assertEqual(last_occurence_char('abc', 'b'), 2)

    def test_char_not_present(self):
        self.assertIsNone(last_occurence_char('abc', 'x'))
