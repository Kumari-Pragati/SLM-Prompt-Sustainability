import unittest
from mbpp_442_code import positive_count

class TestPositiveCount(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertAlmostEqual(positive_count([1, 2, 3, 4]), 1.0)

    def test_zero_numbers(self):
        self.assertAlmostEqual(positive_count([0, 0, 0]), 0.0)

    def test_negative_numbers(self):
        self.assertAlmostEqual(positive_count([-1, -2, -3]), 0.0)

    def test_empty_list(self):
        self.assertAlmostEqual(positive_count([]), 0.0)

    def test_single_zero(self):
        self.assertAlmostEqual(positive_count([0]), 0.0)

    def test_single_positive(self):
        self.assertAlmostEqual(positive_count([1]), 1.0)

    def test_single_negative(self):
        self.assertAlmostEqual(positive_count([-1]), 0.0)
