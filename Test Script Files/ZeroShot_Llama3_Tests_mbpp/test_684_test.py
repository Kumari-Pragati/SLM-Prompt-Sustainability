import unittest
from mbpp_684_code import count_Char

class TestCountChar(unittest.TestCase):

    def test_count_Char(self):
        self.assertEqual(count_Char("hello", "o"), 2)
        self.assertEqual(count_Char("hello", "h"), 1)
        self.assertEqual(count_Char("hello", "l"), 2)
        self.assertEqual(count_Char("hello", "e"), 1)
        self.assertEqual(count_Char("hello", "x"), 0)
        self.assertEqual(count_Char("hello", "H"), 0)
        self.assertEqual(count_Char("hello", "L"), 0)
        self.assertEqual(count_Char("hello", "E"), 0)
        self.assertEqual(count_Char("hello", "o", 15), 3)
        self.assertEqual(count_Char("hello", "o", 20), 4)
        self.assertEqual(count_Char("hello", "o", 25), 5)

    def test_count_Char_edge_cases(self):
        self.assertEqual(count_Char("", "o"), 0)
        self.assertEqual(count_Char("a", "o"), 0)
        self.assertEqual(count_Char("o", "o"), 1)
        self.assertEqual(count_Char("ooo", "o"), 3)
        self.assertEqual(count_Char("hello", "o", 0), 0)
