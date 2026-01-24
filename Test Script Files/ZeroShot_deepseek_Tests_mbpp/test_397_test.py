import unittest
from mbpp_397_code import median_numbers

class TestMedianNumbers(unittest.TestCase):

    def test_median_numbers(self):
        self.assertEqual(median_numbers(1, 2, 3), 2)
        self.assertEqual(median_numbers(3, 2, 1), 2)
        self.assertEqual(median_numbers(1, 3, 2), 2)
        self.assertEqual(median_numbers(2, 2, 2), 2)
        self.assertEqual(median_numbers(1, 1, 1), 1)
        self.assertEqual(median_numbers(10, 20, 30), 20)
        self.assertEqual(median_numbers(30, 20, 10), 20)
        self.assertEqual(median_numbers(10, 30, 20), 20)
        self.assertEqual(median_numbers(20, 20, 30), 20)
        self.assertEqual(median_numbers(30, 30, 30), 30)
