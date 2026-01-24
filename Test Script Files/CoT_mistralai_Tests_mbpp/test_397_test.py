import unittest
from mbpp_397_code import median_numbers

class TestMedianNumbers(unittest.TestCase):
    def test_median_with_three_numbers(self):
        self.assertEqual(median_numbers(1, 2, 3), 2)
        self.assertEqual(median_numbers(3, 2, 1), 2)
        self.assertEqual(median_numbers(2, 3, 1), 2)

    def test_median_with_two_numbers(self):
        self.assertEqual(median_numbers(1, 2), 1.5)
        self.assertEqual(median_numbers(2, 1), 1.5)

    def test_median_with_equal_numbers(self):
        self.assertEqual(median_numbers(1, 1, 1), 1)
        self.assertEqual(median_numbers(2, 2, 2), 2)

    def test_median_with_negative_numbers(self):
        self.assertEqual(median_numbers(-1, -2, -3), -1.5)
        self.assertEqual(median_numbers(-3, -2, -1), -2)

    def test_median_with_zero(self):
        self.assertEqual(median_numbers(0, 1, 2), 1)
        self.assertEqual(median_numbers(1, 0, 2), 1)
        self.assertEqual(median_numbers(1, 2, 0), 1)
        self.assertEqual(median_numbers(0, 0, 0), 0)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, median_numbers, 'a', 1, 2)
        self.assertRaises(TypeError, median_numbers, 1, 'b', 2)
        self.assertRaises(TypeError, median_numbers, 1, 2, 'c')
