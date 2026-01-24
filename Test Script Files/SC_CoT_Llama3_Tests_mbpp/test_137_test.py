import unittest
from mbpp_137_code import zero_count

class TestZeroCount(unittest.TestCase):
    def test_zero_count_typical(self):
        self.assertEqual(zero_count([0, 1, 2, 0, 3, 4, 0]), 3/7)

    def test_zero_count_all_zeros(self):
        self.assertEqual(zero_count([0, 0, 0, 0, 0]), 1)

    def test_zero_count_all_non_zeros(self):
        self.assertEqual(zero_count([1, 2, 3, 4, 5]), 0)

    def test_zero_count_mixed(self):
        self.assertEqual(zero_count([0, 1, 2, 3, 4, 0]), 2/6)

    def test_zero_count_empty_list(self):
        self.assertEqual(zero_count([]), 0)

    def test_zero_count_single_zero(self):
        self.assertEqual(zero_count([0]), 1)

    def test_zero_count_single_non_zero(self):
        self.assertEqual(zero_count([1]), 0)

    def test_zero_count_multiple_zeros(self):
        self.assertEqual(zero_count([0, 0, 0, 0, 0, 0]), 6/6)

    def test_zero_count_multiple_non_zeros(self):
        self.assertEqual(zero_count([1, 2, 3, 4, 5, 6]), 0)
