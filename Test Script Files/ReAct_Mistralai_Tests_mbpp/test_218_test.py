import unittest
from mbpp_218_code import min_Operations

class TestMinOperations(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_Operations(12, 16), 3)
        self.assertEqual(min_Operations(20, 24), 3)
        self.assertEqual(min_Operations(36, 48), 7)

    def test_edge_cases(self):
        self.assertEqual(min_Operations(1, 1), 0)
        self.assertEqual(min_Operations(2, 2), 0)
        self.assertEqual(min_Operations(1, 2), 1)
        self.assertEqual(min_Operations(0, 1), 0)
        self.assertEqual(min_Operations(1, 0), 0)

    def test_gcd_and_swap(self):
        self.assertEqual(min_Operations(18, 24), 5)  # gcd(18, 24) = 6
        self.assertEqual(min_Operations(18, 36), 15)  # gcd(18, 36) = 6
        self.assertEqual(min_Operations(36, 18), 15)  # swapped arguments

    def test_negative_numbers(self):
        self.assertRaises(ValueError, min_Operations, -1, -2)
        self.assertRaises(ValueError, min_Operations, -1, 0)
        self.assertRaises(ValueError, min_Operations, 0, -1)
