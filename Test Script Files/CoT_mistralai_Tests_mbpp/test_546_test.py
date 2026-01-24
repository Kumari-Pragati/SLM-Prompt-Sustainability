import unittest
from mbpp_546_code import last_occurence_char

class TestLastOccurenceChar(unittest.TestCase):
    def test_empty_string(self):
        self.assertIsNone(last_occurence_char('', 'a'))

    def test_single_char_string(self):
        self.assertIsNone(last_occurence_char('a', 'b'))
        self.assertEqual(last_occurence_char('a', 'a'), 1)

    def test_multiple_chars_string(self):
        self.assertEqual(last_occurence_char('abcabc', 'c'), 5)
        self.assertEqual(last_occurence_char('abcabc', 'a'), 0)

    def test_repeated_char_string(self):
        self.assertEqual(last_occurence_char('aaaa', 'a'), 4)

    def test_multi_char_single_occurence(self):
        self.assertEqual(last_occurence_char('abcdefg', 'x'), None)

    def test_invalid_input_string(self):
        self.assertRaises(TypeError, last_occurence_char, 123, 'a')
        self.assertRaises(TypeError, last_occurence_char, 'str', 1)
