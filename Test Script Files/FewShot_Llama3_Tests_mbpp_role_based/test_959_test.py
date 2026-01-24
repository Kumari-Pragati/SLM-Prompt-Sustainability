import unittest
from mbpp_959_code import Average

class TestAverage(unittest.TestCase):
    def test_average_of_positive_numbers(self):
        self.assertAlmostEqual(Average([1, 2, 3, 4, 5]), 3)

    def test_average_of_negative_numbers(self):
        self.assertAlmostEqual(Average([-1, -2, -3, -4, -5]), -3)

    def test_average_of_mixed_numbers(self):
        self.assertAlmostEqual(Average([1, -2, 3, -4, 5]), 1)

    def test_average_of_zero(self):
        self.assertAlmostEqual(Average([0, 0, 0, 0, 0]), 0)

    def test_average_of_empty_list(self):
        with self.assertRaises(ZeroDivisionError):
            Average([])

    def test_average_of_single_element(self):
        self.assertEqual(Average([1]), 1)

    def test_average_of_float_numbers(self):
        self.assertAlmostEqual(Average([1.0, 2.0, 3.0, 4.0, 5.0]), 3)
