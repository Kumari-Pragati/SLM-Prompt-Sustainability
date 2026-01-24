import unittest
from mbpp_911_code import maximum_product

class TestMaximumProduct(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(maximum_product([]), 0)

    def test_single_element(self):
        self.assertEqual(maximum_product([1]), 1)

    def test_two_elements(self):
        self.assertEqual(maximum_product([1, 2]), 2)

    def test_three_elements(self):
        self.assertEqual(maximum_product([1, 2, 3]), 6)

    def test_negative_numbers(self):
        self.assertEqual(maximum_product([-1, -2, -3]), 6)

    def test_large_numbers(self):
        self.assertEqual(maximum_product([1000, 2000, 3000]), 6000000)

    def test_duplicates(self):
        self.assertEqual(maximum_product([1, 1, 2]), 2)
