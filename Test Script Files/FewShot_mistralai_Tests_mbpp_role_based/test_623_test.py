import unittest
from mbpp_623_code import nth_nums

class TestNthNums(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(nth_nums([1, 2, 3, 4], 2), [1, 4, 9, 16])

    def test_zero_base(self):
        self.assertEqual(nth_nums([1, 2, 3, 4], 0), [1, 1, 1, 1])

    def test_negative_numbers(self):
        self.assertEqual(nth_nums([-1, -2, -3, -4], 3), [(-1)**3, (-2)**3, (-3)**3, (-4)**3])

    def test_empty_list(self):
        self.assertListEqual(nth_nums([], 2), [])

    def test_negative_exponent(self):
        with self.assertRaises(ValueError):
            nth_nums([1, 2, 3, 4], -1)
