import unittest
from mbpp_476_code import big_sum

class TestBigSum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(big_sum([1, 2, 3, 4, 5]), 1 + 5)

    def test_single_element(self):
        self.assertEqual(big_sum([1]), 1)

    def test_empty_list(self):
        self.assertEqual(big_sum([]), None)

    def test_negative_numbers(self):
        self.assertEqual(big_sum([-1, -2, -3]), -1 + -3)

    def test_min_greater_max(self):
        self.assertEqual(big_sum([5, 2]), 5)
