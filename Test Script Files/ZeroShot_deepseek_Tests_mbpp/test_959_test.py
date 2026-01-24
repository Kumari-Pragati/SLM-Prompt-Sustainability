import unittest
from mbpp_959_code import Average

class TestAverage(unittest.TestCase):

    def test_average_with_positive_numbers(self):
        self.assertAlmostEqual(Average([1, 2, 3, 4, 5]), 3.0)

    def test_average_with_negative_numbers(self):
        self.assertAlmostEqual(Average([-1, -2, -3, -4, -5]), -3.0)

    def test_average_with_mixed_numbers(self):
        self.assertAlmostEqual(Average([-1, 2, -3, 4, -5]), 0.0)

    def test_average_with_zeroes(self):
        self.assertAlmostEqual(Average([0, 0, 0, 0, 0]), 0.0)

    def test_average_with_single_number(self):
        self.assertAlmostEqual(Average([5]), 5.0)

    def test_average_with_empty_list(self):
        with self.assertRaises(ZeroDivisionError):
            Average([])
