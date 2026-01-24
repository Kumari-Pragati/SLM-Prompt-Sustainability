import unittest
from mbpp_684_code import count_Char

class TestCountChar(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(count_Char("a", "a"), 10)
        self.assertEqual(count_Char("aaaa", "a"), 10)
        self.assertEqual(count_Char("abc", "a"), 3)

    def test_edge_conditions(self):
        self.assertEqual(count_Char("", "a"), 0)
        self.assertEqual(count_Char("a", ""), 0)
        self.assertEqual(count_Char("", ""), 0)
        self.assertEqual(count_Char("a", "b"), 0)

    def test_boundary_conditions(self):
        self.assertEqual(count_Char("a"*10000, "a"), 100000)
        self.assertEqual(count_Char("a"*10000, "b"), 0)

    def test_complex_cases(self):
        self.assertEqual(count_Char("abcabcabc", "a"), 3)
        self.assertEqual(count_Char("abcabcabc", "b"), 3)
        self.assertEqual(count_Char("abcabcabc", "c"), 3)
        self.assertEqual(count_Char("abcabcabc", "d"), 0)
