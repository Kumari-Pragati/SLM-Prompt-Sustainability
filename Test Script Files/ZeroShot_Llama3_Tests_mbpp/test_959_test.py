import unittest
from mbpp_959_code import Average

class TestAverage(unittest.TestCase):

    def test_average_with_positive_numbers(self):
        self.assertEqual(Average([1, 2, 3, 4, 5]), 3)

    def test_average_with_negative_numbers(self):
        self.assertEqual(Average([-1, -2, -3, -4, -5]), -3)

    def test_average_with_mixed_numbers(self):
        self.assertEqual(Average([1, -2, 3, -4, 5]), 1)

    def test_average_with_zero(self):
        self.assertEqual(Average([0, 0, 0, 0, 0]), 0)

    def test_average_with_empty_list(self):
        with self.assertRaises(ZeroDivisionError):
            Average([])

    def test_average_with_single_element(self):
        self.assertEqual(Average([5]), 5)

    def test_average_with_float_numbers(self):
        self.assertAlmostEqual(Average([1.5, 2.5, 3.5, 4.5, 5.5]), 3.5)
