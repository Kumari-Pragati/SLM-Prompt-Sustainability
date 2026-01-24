import unittest
from mbpp_573_code import unique_product

class TestUniqueProduct(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(unique_product([]), 1)

    def test_single_element_list(self):
        self.assertEqual(unique_product([1]), 1)

    def test_positive_numbers(self):
        self.assertEqual(unique_product([1, 2, 3]), 6)

    def test_negative_numbers(self):
        self.assertEqual(unique_product([-1, -2, -3]), 6)

    def test_mixed_numbers(self):
        self.assertEqual(unique_product([1, -2, 3]), 6)

    def test_duplicates(self):
        self.assertEqual(unique_product([1, 1, 2, 3]), 2)

    def test_zero(self):
        self.assertEqual(unique_product([0, 1, 2]), 0)
