import unittest
from mbpp_546_code import last_occurence_char

class TestLastOccurenceChar(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(last_occurence_char("abc", "a"), 1)
        self.assertEqual(last_occurence_char("abc", "b"), 2)
        self.assertEqual(last_occurence_char("abc", "c"), 3)
        self.assertEqual(last_occurence_char("abc", "d"), None)

    def test_edge(self):
        self.assertEqual(last_occurence_char("", "a"), None)
        self.assertEqual(last_occurence_char("a", "a"), 1)
        self.assertEqual(last_occurence_char("abc", "b"), 1)
        self.assertEqual(last_occurence_char("abc", "c"), 2)

    def test_complex(self):
        self.assertEqual(last_occurence_char("abcabc", "a"), 4)
        self.assertEqual(last_occurence_char("abcabc", "b",), 2)
        self.assertEqual(last_occurence_char("abcabc", "c"), 3)
