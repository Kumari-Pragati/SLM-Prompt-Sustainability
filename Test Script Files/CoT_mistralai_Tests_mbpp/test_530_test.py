import unittest
from mbpp_530_code import negative_count

class TestNegativeCount(unittest.TestCase):

    def test_empty_list(self):
        self.assertAlmostEqual(negative_count([]), 0.0)

    def test_all_positive(self):
        self.assertAlmostEqual(negative_count([1, 2, 3, 4]), 0.0)

    def test_all_negative(self):
        self.assertAlmostEqual(negative_count([-1, -2, -3, -4]), 1.0)

    def test_mixed_numbers(self):
        self.assertAlmostEqual(negative_count([1, -2, 3, -4, 5]), 0.4)

    def test_single_negative(self):
        self.assertAlmostEqual(negative_count([-1]), 1.0)

    def test_single_positive(self):
        self.assertAlmostEqual(negative_count([1]), 0.0)

    def test_large_list(self):
        nums = [i for i in range(-10000, 10001)]
        self.assertAlmostEqual(negative_count(nums), 0.5)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            negative_count(1.23)
