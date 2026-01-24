import unittest
from mbpp_838_code import min_Swaps

class TestMinSwaps(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(min_Swaps("001010", "101001"), 2)
        self.assertEqual(min_Swaps("101010", "010101"), 2)
        self.assertEqual(min_Swaps("010101", "101010"), 2)
        self.assertEqual(min_Swaps("111111", "000000"), 4)
        self.assertEqual(min_Swaps("000000", "111111"), 4)

    def test_edge_case(self):
        self.assertEqual(min_Swaps("000000", "11111"), 3)
        self.assertEqual(min_Swaps("11111", "00000"), 3)
        self.assertEqual(min_Swaps("010101", "101010"), -1)
        self.assertEqual(min_Swaps("001010", "101001"), -1)
        self.assertEqual(min_Swaps("00000", "11111"), -1)
        self.assertEqual(min_Swaps("11111", "00000"), -1)
        self.assertEqual(min_Swaps("0000", "1111"), -1)
        self.assertEqual(min_Swaps("1111", "0000"), -1)

    def test_invalid_input(self):
        self.assertRaises(ValueError, min_Swaps, "00101", "10100")
        self.assertRaises(ValueError, min_Swaps, "00101", "10100x")
        self.assertRaises(ValueError, min_Swaps, "00101", 10100)
        self.assertRaises(ValueError, min_Swaps, "00101x", "10100")
        self.assertRaises(ValueError, min_Swaps, "00101", "10100", "invalid_function")
