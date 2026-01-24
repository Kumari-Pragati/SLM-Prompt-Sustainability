import unittest
from mbpp_137_code import zero_count

class TestZeroCount(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(zero_count([0, 1, 0, 2, 0]), 0.6, places=2)

    def test_all_zeros(self):
        self.assertAlmostEqual(zero_count([0, 0, 0, 0, 0]), 1.0, places=2)

    def test_all_non_zeros(self):
        self.assertAlmostEqual(zero_count([1, 2, 3, 4, 5]), 0.0, places=2)

    def test_empty_list(self):
        self.assertEqual(zero_count([]), 0.0)

    def test_single_zero(self):
        self.assertAlmostEqual(zero_count([0]), 1.0, places=2)

    def test_single_non_zero(self):
        self.assertAlmostEqual(zero_count([1]), 0.0, places=2)

    def test_negative_numbers(self):
        self.assertAlmostEqual(zero_count([-1, 0, 1]), 0.33, places=2)

    def test_large_numbers(self):
        self.assertAlmostEqual(zero_count([1000, 0, 2000]), 0.33, places=2)

    def test_float_numbers(self):
        self.assertAlmostEqual(zero_count([0.5, 0, 1.5]), 0.5, places=2)
