import unittest
from mbpp_442_code import positive_count

class TestPositiveCount(unittest.TestCase):

    def test_empty_list(self):
        self.assertAlmostEqual(positive_count([]), 0.00)

    def test_all_positive(self):
        self.assertAlmostEqual(positive_count([1, 2, 3, 4, 5]), 1.00)

    def test_mixed_numbers(self):
        self.assertAlmostEqual(positive_count([1, -2, 3, -4, 5]), 3/5)

    def test_zero_in_list(self):
        self.assertAlmostEqual(positive_count([0, 1, -2, 3, -4, 5]), 3/6)

    def test_large_numbers(self):
        self.assertAlmostEqual(positive_count(array('i', [2147483647, -2147483648, 1, -2147483647, 0]))), 1/3)

    def test_negative_list(self):
        self.assertAlmostEqual(positive_count([-1, -2, -3, -4, -5]), 0.00)
