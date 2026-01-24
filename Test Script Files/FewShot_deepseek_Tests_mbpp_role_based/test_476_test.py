import unittest
from mbpp_476_code import big_sum

class TestBigSum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(big_sum([1, 2, 3, 4, 5]), 6)

    def test_edge_condition(self):
        self.assertEqual(big_sum([-1000000000, 1000000000]), 2000000000)

    def test_boundary_condition(self):
        self.assertEqual(big_sum([0, 0]), 0)

    def test_single_element(self):
        self.assertEqual(big_sum([5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(big_sum([-1, -2, -3, -4, -5]), -1)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            big_sum([])
