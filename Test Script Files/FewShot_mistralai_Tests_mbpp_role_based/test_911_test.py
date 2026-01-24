import unittest
from mbpp_911_code import maximum_product

class TestMaximumProduct(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(maximum_product([1, 2, 3, 4, 5]), 120)
        self.assertEqual(maximum_product([6, 7, 8, 9, 10]), 240)

    def test_empty_list(self):
        self.assertEqual(maximum_product([]), 0)

    def test_single_number(self):
        self.assertEqual(maximum_product([1]), 1)

    def test_negative_numbers(self):
        self.assertEqual(maximum_product([-1, -2, -3, -4, -5]), -120)

    def test_mixed_numbers(self):
        self.assertEqual(maximum_product([1, -2, 3, -4, 5]), 15)

    def test_duplicates(self):
        self.assertEqual(maximum_product([1, 1, 2, 3, 4]), 12)
