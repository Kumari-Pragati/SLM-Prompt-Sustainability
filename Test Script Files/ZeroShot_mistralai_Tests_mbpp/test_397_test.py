import unittest
from mbpp_397_code import median_numbers

class TestMedianNumbers(unittest.TestCase):

    def test_median_numbers(self):
        self.assertEqual(median_numbers(1, 2, 3), 2)
        self.assertEqual(median_numbers(1, 2, 1), 1)
        self.assertEqual(median_numbers(3, 2, 1), 2)
        self.assertEqual(median_numbers(3, 3, 2), 3)
        self.assertEqual(median_numbers(2, 2, 2), 2)
        self.assertEqual(median_numbers(-1, 0, 1), 0)
        self.assertEqual(median_numbers(0, -1, 1), -1)
        self.assertEqual(median_numbers(0, 0, -1), -1)
        self.assertEqual(median_numbers(1, -1, -1), -1)
        self.assertEqual(median_numbers(-1, -1, 1), -1)
        self.assertEqual(median_numbers(-1, -1, -1), -1)
