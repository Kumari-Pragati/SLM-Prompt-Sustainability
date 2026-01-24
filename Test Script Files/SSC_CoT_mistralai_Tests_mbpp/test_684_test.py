import unittest
from mbpp_684_code import range
from six.moves import zip_longest

from684_code import count_Char

class TestCountChar(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(count_Char("abc", "a"), 3)
        self.assertEqual(count_Char("aaa", "a"), 3)
        self.assertEqual(count_Char("ABCabc", "a"), 4)
        self.assertEqual(count_Char("12345", "5"), 2)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_Char("", "a"), 0)
        self.assertEqual(count_Char("a", "a"), 1)
        self.assertEqual(count_Char("abcdefghijklmnopqrstuvwxyz", "z"), 1)
        self.assertEqual(count_Char("abcdefghijklmnopqrstuvwxyz", "aa"), 0)
        self.assertEqual(count_Char("a" * 10000, "a"), 10000)

    def test_special_cases(self):
        self.assertEqual(count_Char("a\nb", "a"), 1)
        self.assertEqual(count_Char("a\nb", "b"), 1)
        self.assertEqual(count_Char("a\nb", "\n"), 1)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, count_Char, 1, "a")
        self.assertRaises(TypeError, count_Char, "a", 1.5)
