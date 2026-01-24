import unittest
from mbpp_959_code import Average

class TestAverageFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(Average([1, 2, 3, 4, 5]), 3.0)

    def test_single_element(self):
        self.assertEqual(Average([5]), 5)

    def test_empty_list(self):
        with self.assertRaises(ZeroDivisionError):
            Average([])

    def test_negative_numbers(self):
        self.assertAlmostEqual(Average([-1, -2, -3, -4, -5]), -3.0)

    def test_decimal_numbers(self):
        self.assertAlmostEqual(Average([1.5, 2.5, 3.5]), 2.5)

    def test_large_numbers(self):
        self.assertAlmostEqual(Average(list(range(1, 10001))), 5000.5)

    def test_float_and_int(self):
        self.assertAlmostEqual(Average([1, 2, 3, 4.5]), 2.625)
