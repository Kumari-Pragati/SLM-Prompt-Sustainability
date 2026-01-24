import unittest
from mbpp_959_code import Average

class TestAverageFunction(unittest.TestCase):

    def test_average_typical_case(self):
        self.assertAlmostEqual(Average([1, 2, 3, 4, 5]), 3.0)

    def test_average_single_element(self):
        self.assertEqual(Average([5]), 5)

    def test_average_empty_list(self):
        with self.assertRaises(ZeroDivisionError):
            Average([])

    def test_average_negative_numbers(self):
        self.assertAlmostEqual(Average([-1, -2, -3, -4, -5]), -3.0)

    def test_average_decimal_numbers(self):
        self.assertAlmostEqual(Average([1.5, 2.5, 3.5]), 2.5)

    def test_average_large_numbers(self):
        self.assertAlmostEqual(Average(list(range(1, 10001))), 5000.5)

    def test_average_non_integer_list(self):
        self.assertAlmostEqual(Average([1.0, 2.0, 3.0]), 2.0)
