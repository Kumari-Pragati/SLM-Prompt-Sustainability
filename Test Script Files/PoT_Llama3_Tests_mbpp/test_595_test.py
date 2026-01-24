import unittest
from mbpp_595_code import min_Swaps

class TestMinSwaps(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_Swaps("abc", "def"), 2)

    def test_edge_case(self):
        self.assertEqual(min_Swaps("abc", "abc"), 0)
        self.assertEqual(min_Swaps("abc", "abcd"), 1)
        self.assertEqual(min_Swaps("abcd", "abc"), 1)

    def test_corner_case(self):
        self.assertEqual(min_Swaps("abc", "bca"), 2)
        self.assertEqual(min_Swaps("abc", "cab"), 2)
        self.assertEqual(min_Swaps("abc", "acb"), 2)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            min_Swaps(123, "abc")
        with self.assertRaises(TypeError):
            min_Swaps("abc", 123)
