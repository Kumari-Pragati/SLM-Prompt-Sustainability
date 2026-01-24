import unittest
from mbpp_684_code import count_Char

class TestCountChar(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(count_Char("abc", "a"), 3)
        self.assertEqual(count_Char("", "a"), 0)
        self.assertEqual(count_Char("aa", "a"), 2)
        self.assertEqual(count_Char("abab", "a"), 4)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_Char("a" * 1000, "a"), 1000)
        self.assertEqual(count_Char("a" * 1001, "a"), 1000)
        self.assertEqual(count_Char("z" * 1000, "z"), 1000)
        self.assertEqual(count_Char("", "a"), 0)
        self.assertEqual(count_Char("a", "b"), 0)

    def test_complex_scenarios(self):
        self.assertEqual(count_Char("AABA", "A"), 3)
        self.assertEqual(count_Char("AABA", "B"), 1)
        self.assertEqual(count_Char("AABA", "a"), 0)
        self.assertEqual(count_Char("AABA", " "), 0)
