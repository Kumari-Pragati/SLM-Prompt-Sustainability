import unittest
from mbpp_137_code import zero_count

class TestZeroCount(unittest.TestCase):
    def test_zero_count_empty_list(self):
        self.assertEqual(zero_count([]), 0.0)

    def test_zero_count_all_zeros(self):
        self.assertEqual(zero_count([0, 0, 0, 0]), 1.0)

    def test_zero_count_all_non_zeros(self):
        self.assertEqual(zero_count([1, 2, 3, 4]), 0.0)

    def test_zero_count_mixed_numbers(self):
        self.assertAlmostEqual(zero_count([0, 1, 0, 2, 0]), 0.5)

    def test_zero_count_single_zero(self):
        self.assertEqual(zero_count([0]), 1.0)

    def test_zero_count_single_non_zero(self):
        self.assertEqual(zero_count([1]), 0.0)
