import unittest
from mbpp_573_code import unique_product

class TestUniqueProduct(unittest.TestCase):

    def test_unique_product_with_positive_numbers(self):
        self.assertEqual(unique_product([1, 2, 3, 4, 5]), 120)

    def test_unique_product_with_negative_numbers(self):
        self.assertEqual(unique_product([-1, -2, -3, -4, -5]), -120)

    def test_unique_product_with_mixed_numbers(self):
        self.assertEqual(unique_product([-1, 2, -3, 4, -5]), -120)

    def test_unique_product_with_zero(self):
        self.assertEqual(unique_product([0, 1, 2, 3, 4]), 0)

    def test_unique_product_with_single_element(self):
        self.assertEqual(unique_product([5]), 5)

    def test_unique_product_with_empty_list(self):
        self.assertEqual(unique_product([]), 1)

    def test_unique_product_with_duplicates(self):
        self.assertEqual(unique_product([1, 2, 2, 3, 4]), 24)
