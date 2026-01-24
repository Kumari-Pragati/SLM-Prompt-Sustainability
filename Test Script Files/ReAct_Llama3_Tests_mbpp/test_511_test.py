import unittest
from mbpp_511_code import find_Min_Sum

class TestFindMinSum(unittest.TestCase):
    def test_find_min_sum_positive(self):
        self.assertEqual(find_Min_Sum(10), 2)

    def test_find_min_sum_negative(self):
        with self.assertRaises(TypeError):
            find_Min_Sum(-10)

    def test_find_min_sum_zero(self):
        self.assertEqual(find_Min_Sum(0), 0)

    def test_find_min_sum_one(self):
        self.assertEqual(find_Min_Sum(1), 1)

    def test_find_min_sum_prime(self):
        self.assertEqual(find_Min_Sum(23), 2)

    def test_find_min_sum_composite(self):
        self.assertEqual(find_Min_Sum(36), 12)

    def test_find_min_sum_large(self):
        self.assertEqual(find_Min_Sum(1000), 1)
