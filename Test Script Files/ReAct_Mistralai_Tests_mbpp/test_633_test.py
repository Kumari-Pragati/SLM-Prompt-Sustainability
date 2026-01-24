import unittest
from mbpp_633_code import pair_OR_Sum

class TestPairORSum(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(pair_OR_Sum([], 0), 0)

    def test_single_element(self):
        self.assertEqual(pair_OR_Sum([1], 1), 0)

    def test_pair_case(self):
        self.assertEqual(pair_OR_Sum([1, 2], 2), 3)

    def test_multiple_pairs(self):
        self.assertEqual(pair_OR_Sum([1, 2, 3, 4], 4), 15)

    def test_all_same(self):
        self.assertEqual(pair_OR_Sum([1, 1, 1, 1], 4), 0)

    def test_negative_numbers(self):
        self.assertEqual(pair_OR_Sum([-1, -2], 2), 3)

    def test_large_numbers(self):
        self.assertEqual(pair_OR_Sum([1000000001, 1000000002], 2), 1000000003)

    def test_out_of_bounds(self):
        with self.assertRaises(IndexError):
            pair_OR_Sum([1, 2], 3)
