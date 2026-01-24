import unittest
from mbpp_699_code import min_Swaps

class TestMinSwaps(unittest.TestCase):

    def test_min_swaps_even_count(self):
        self.assertEqual(min_Swaps("ABCD", "DCBA"), 1)
        self.assertEqual(min_Swaps("ABCDEFG", "GFEDCBA"), 3)
        self.assertEqual(min_Swaps("A", "B"), 0)
        self.assertEqual(min_Swaps("AA", "BB"), 0)
        self.assertEqual(min_Swaps("AAA", "BBB"), 1)

    def test_min_swaps_odd_count(self):
        self.assertEqual(min_Swaps("ABCD", "CDAB"), "Not Possible")
        self.assertEqual(min_Swaps("ABCDEFG", "GFECDAB"), "Not Possible")
        self.assertEqual(min_Swaps("A", "B", "Not Possible")
        self.assertEqual(min_Swaps("AA", "BB", "AAA", "BBB"), "Not Possible")

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, min_Swaps, 1, 2)
        self.assertRaises(TypeError, min_Swaps, "ABC", 1, 2, 3)
        self.assertRaises(TypeError, min_Swaps, [1, 2, 3], [4, 5, 6])
