import unittest
from mbpp_666_code import count_char

class TestCountChar(unittest.TestCase):

    def test_count_char(self):
        self.assertEqual(count_char("hello", "l"), 2)
        self.assertEqual(count_char("hello", "o"), 1)
        self.assertEqual(count_char("hello", "h"), 1)
        self.assertEqual(count_char("hello", "e"), 1)
        self.assertEqual(count_char("hello", "a"), 0)
        self.assertEqual(count_char("hello", "b"), 0)
        self.assertEqual(count_char("", "a"), 0)
        self.assertEqual(count_char("abc", "a"), 1)
        self.assertEqual(count_char("abc", "b"), 1)
        self.assertEqual(count_char("abc", "c"), 1)
        self.assertEqual(count_char("abc", "d"), 0)

    def test_count_char_edge_cases(self):
        self.assertEqual(count_char("a", "a"), 1)
        self.assertEqual(count_char("a", "b"), 0)
        self.assertEqual(count_char("", "a"), 0)
        self.assertEqual(count_char("a", "a"), 1)
        self.assertEqual(count_char("a", "b"), 0)
        self.assertEqual(count_char("", "a"), 0)
