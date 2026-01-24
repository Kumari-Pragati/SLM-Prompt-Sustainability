import unittest
from mbpp_546_code import last_occurence_char

class TestLastOccurenceChar(unittest.TestCase):

    def test_last_occurence_char_positive(self):
        self.assertEqual(last_occurence_char('hello', 'l'), 5)
        self.assertEqual(last_occurence_char('world', 'o'), 6)
        self.assertEqual(last_occurence_char('python', 'n'), 6)

    def test_last_occurence_char_negative(self):
        self.assertIsNone(last_occurence_char('hello', 'z'))
        self.assertIsNone(last_occurence_char('world', 'i'))
        self.assertIsNone(last_occurence_char('python', 'j'))

    def test_last_occurence_char_edge_cases(self):
        self.assertEqual(last_occurence_char('', 'a'), None)
        self.assertEqual(last_occurence_char('a', 'a'), 1)
        self.assertEqual(last_occurence_char('aaa', 'a'), 3)
