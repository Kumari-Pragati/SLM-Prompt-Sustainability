import unittest
from mbpp_471_code import find_remainder

class TestFindRemainder(unittest.TestCase):

    def test_find_remainder_positive_numbers(self):
        self.assertEqual(find_remainder([1, 2, 3], 3, 4), 0)
        self.assertEqual(find_remainder([1, 2, 3, 4], 4, 5), 1)
        self.assertEqual(find_remainder([10, 20, 30, 40], 4, 100), 0)

    def test_find_remainder_negative_numbers(self):
        self.assertEqual(find_remainder([-1, -2, -3], 3, 4), 3)
        self.assertEqual(find_remainder([-1, -2, -3, -4], 4, 5), 1)
        self.assertEqual(find_remainder([-10, -20, -30, -40], 4, 100), 0)

    def test_find_remainder_mixed_numbers(self):
        self.assertEqual(find_remainder([-1, 2, -3, 4], 4, 5), 1)
        self.assertEqual(find_remainder([10, -20, 30, -40], 4, 100), 0)

    def test_find_remainder_large_numbers(self):
        self.assertEqual(find_remainder([10**10, 20**10, 30**10, 40**10], 4, 10**100), 0)

    def test_find_remainder_zero_length(self):
        self.assertEqual(find_remainder([], 0, 10), 0)
