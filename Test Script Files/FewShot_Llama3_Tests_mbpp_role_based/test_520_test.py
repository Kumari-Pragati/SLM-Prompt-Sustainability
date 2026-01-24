import unittest
from mbpp_520_code import get_lcm

class TestGetLcm(unittest.TestCase):
    def test_single_pair(self):
        self.assertEqual(get_lcm([2, 3]), 6)

    def test_multiple_pairs(self):
        self.assertEqual(get_lcm([2, 3, 4, 5]), 60)

    def test_single_pair_with_zero(self):
        with self.assertRaises(IndexError):
            get_lcm([0, 1])

    def test_single_pair_with_negative(self):
        self.assertEqual(get_lcm([-2, 3]), 6)

    def test_multiple_pairs_with_mixed_signs(self):
        self.assertEqual(get_lcm([-2, 3, 4, 5]), 60)

    def test_empty_list(self):
        with self.assertRaises(IndexError):
            get_lcm([])
