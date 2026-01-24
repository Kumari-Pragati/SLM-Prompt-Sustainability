import unittest
from mbpp_838_code import min_Swaps

class TestMinSwaps(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(min_Swaps("0001101", "1100010"), 2)
        self.assertEqual(min_Swaps("10101010", "11111111"), 6)
        self.assertEqual(min_Swaps("01010101", "11100000"), 4)

    def test_edge_cases(self):
        self.assertEqual(min_Swaps("0", "1"), 0)
        self.assertEqual(min_Swaps("1", "0"), 0)
        self.assertEqual(min_Swaps("00", "11"), 0)
        self.assertEqual(min_Swaps("11", "00"), 0)
        self.assertEqual(min_Swaps("01010101", "11111111"), 6)
        self.assertEqual(min_Swaps("11111111", "01010101"), 6)

    def test_corner_cases(self):
        self.assertEqual(min_Swaps("0000000", "1111111"), 8)
        self.assertEqual(min_Swaps("1111111", "0000000"), 8)
        self.assertEqual(min_Swaps("0000000", "0000000"), 0)
        self.assertEqual(min_Swaps("1111111", "1111111"), 0)
        self.assertEqual(min_Swaps("01010101", "01010101"), -1)
        self.assertEqual(min_Swaps("11111111", "0"), -1)
        self.assertEqual(min_Swaps("", ""), -1)
        self.assertEqual(min_Swaps("1", "00"), -1)
        self.assertEqual(min_Swaps("0", "100"), -1)
