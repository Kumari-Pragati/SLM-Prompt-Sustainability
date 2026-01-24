import unittest
from mbpp_838_code import min_Swaps

class TestMinSwaps(unittest.TestCase):

    def test_min_swaps_empty_strings(self):
        self.assertEqual(min_Swaps("", ""), 0)

    def test_min_swaps_same_strings(self):
        self.assertEqual(min_Swaps("000", "000"), 0)
        self.assertEqual(min_Swaps("111", "111"), 0)

    def test_min_swaps_different_lengths(self):
        self.assertRaises(ValueError, min_Swaps, "000", "00")
        self.assertRaises(ValueError, min_Swaps, "00", "000")

    def test_min_swaps_single_swap(self):
        self.assertEqual(min_Swaps("010", "100"), 1)
        self.assertEqual(min_Swaps("100", "010"), 1)

    def test_min_swaps_multiple_swaps(self):
        self.assertEqual(min_Swaps("001010", "101001"), 3)
        self.assertEqual(min_Swaps("101001", "001010"), 3)

    def test_min_swaps_edge_cases(self):
        self.assertEqual(min_Swaps("010101", "101010"), 2)
        self.assertEqual(min_Swaps("101010", "010101"), 2)
        self.assertEqual(min_Swaps("000001", "111110"), 5)
        self.assertEqual(min_Swaps("111110", "000001"), 5)
