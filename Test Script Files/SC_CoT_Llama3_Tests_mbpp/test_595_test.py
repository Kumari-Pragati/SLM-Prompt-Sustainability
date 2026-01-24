import unittest
from mbpp_595_code import min_Swaps

class TestMinSwaps(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(min_Swaps("abc", "abc"), 0)
        self.assertEqual(min_Swaps("abc", "abcd"), 1)
        self.assertEqual(min_Swaps("abc", "def"), 3)

    def test_edge_cases(self):
        self.assertEqual(min_Swaps("a", "a"), 0)
        self.assertEqual(min_Swaps("a", "b"), 1)
        self.assertEqual(min_Swaps("a", "aa"), 1)

    def test_boundary_cases(self):
        self.assertEqual(min_Swaps("", ""), 0)
        self.assertEqual(min_Swaps("a", ""), "Not Possible")
        self.assertEqual(min_Swaps("", "a"), "Not Possible")

    def test_special_cases(self):
        self.assertEqual(min_Swaps("abc", "cab"), 1)
        self.assertEqual(min_Swaps("abc", "acb"), 1)
        self.assertEqual(min_Swaps("abc", "bca"), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            min_Swaps(123, "abc")
        with self.assertRaises(TypeError):
            min_Swaps("abc", 123)
