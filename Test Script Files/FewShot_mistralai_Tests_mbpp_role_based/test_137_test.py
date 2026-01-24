import unittest
from mbpp_137_code import zero_count

class TestZeroCount(unittest.TestCase):
    def test_zero_in_list(self):
        self.assertAlmostEqual(zero_count([0, 1, 2, 0, 3]), 0.4)

    def test_all_zeros(self):
        self.assertAlmostEqual(zero_count([0, 0, 0]), 1.0)

    def test_empty_list(self):
        self.assertAlmostEqual(zero_count([]), 0.0)

    def test_negative_numbers(self):
        self.assertAlmostEqual(zero_count([-1, 0, -2]), 0.333)

    def test_floating_point_numbers(self):
        self.assertAlmostEqual(zero_count([0.1, 0.2, 0.3, 0.4]), 1.0)
