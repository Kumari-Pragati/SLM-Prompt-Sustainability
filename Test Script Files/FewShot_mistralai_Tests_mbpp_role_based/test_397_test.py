import unittest
from mbpp_397_code import median_numbers

class TestMedianNumbers(unittest.TestCase):
    def test_median_of_three_numbers(self):
        self.assertEqual(median_numbers(1, 2, 3), 2)
        self.assertEqual(median_numbers(3, 2, 1), 2)
        self.assertEqual(median_numbers(-1, 0, 1), 0)
        self.assertEqual(median_numbers(1, 0, -1), 0)
        self.assertEqual(median_numbers(2, 2, 2), 2)

    def test_median_of_two_numbers(self):
        self.assertEqual(median_numbers(1, 2), 1.5)
        self.assertEqual(median_numbers(2, 1), 1.5)

    def test_median_of_one_number(self):
        self.assertEqual(median_numbers(1), 1)

    def test_median_of_empty_list(self):
        with self.assertRaises(ValueError):
            median_numbers([])

    def test_median_of_negative_numbers(self):
        self.assertEqual(median_numbers(-1, -2, -3), -1.5)
        self.assertEqual(median_numbers(-3, -2, -1), -2.0)
