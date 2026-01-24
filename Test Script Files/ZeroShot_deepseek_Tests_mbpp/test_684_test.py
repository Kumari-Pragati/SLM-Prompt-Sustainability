import unittest
from mbpp_684_code import count_Char

class TestCountChar(unittest.TestCase):

    def test_count_Char(self):
        self.assertEqual(count_Char('abc', 'a'), 1)
        self.assertEqual(count_Char('abc', 'b'), 1)
        self.assertEqual(count_Char('abc', 'c'), 1)
        self.assertEqual(count_Char('abcabcabc', 'a'), 3)
        self.assertEqual(count_Char('abcabcabc', 'b'), 3)
        self.assertEqual(count_Char('abcabcabc', 'c'), 3)
        self.assertEqual(count_Char('abcabcabc', 'd'), 0)
        self.assertEqual(count_Char('abcabcabc', ''), 0)
        self.assertEqual(count_Char('', 'a'), 0)
        self.assertEqual(count_Char('', ''), 0)
        self.assertEqual(count_Char('a', 'a'), 1)
        self.assertEqual(count_Char('a', 'b'), 0)
        self.assertEqual(count_Char('aaa', 'a'), 3)
        self.assertEqual(count_Char('aaa', 'b'), 0)
        self.assertEqual(count_Char('aaa', ''), 0)
        self.assertEqual(count_Char('', ''), 0)
