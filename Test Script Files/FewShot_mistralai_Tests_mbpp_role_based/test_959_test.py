import unittest
from mbpp_959_code import Average

class TestAverage(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertAlmostEqual(Average([1, 2, 3, 4]), 2.5)

    def test_zero_length_list(self):
        self.assertAlmostEqual(Average([]), 0)

    def test_negative_numbers(self):
        self.assertAlmostEqual(Average([-1, -2, -3]), -1.5)

    def test_mixed_numbers(self):
        self.assertAlmostEqual(Average([1, -2, 3]), 1)

    def test_float_numbers(self):
        self.assertAlmostEqual(Average([1.1, 2.2, 3.3]), 2.2)
