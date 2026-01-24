import unittest

from mbpp_959_code import Average

class TestAverage(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(Average([1, 2, 3, 4, 5]), 3.0)

    def test_single_element(self):
        self.assertAlmostEqual(Average([5]), 5.0)

    def test_empty_list(self):
        with self.assertRaises(ZeroDivisionError):
            Average([])

    def test_negative_numbers(self):
        self.assertAlmostEqual(Average([-1, -2, -3, -4, -5]), -3.0)

    def test_decimal_numbers(self):
        self.assertAlmostEqual(Average([1.5, 2.5, 3.5]), 2.5)

    def test_large_numbers(self):
        self.assertAlmostEqual(Average(list(range(1, 10001))), 5000.5)

    def test_non_integer_list(self):
        with self.assertRaises(TypeError):
            Average(['1', 2, 3])

    def test_non_numeric_list(self):
        with self.assertRaises(TypeError):
            Average(['a', 'b', 'c'])
