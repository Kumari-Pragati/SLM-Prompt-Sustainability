import unittest
from mbpp_573_code import unique_product

class TestUniqueProduct(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertEqual(unique_product([1, 2, 3]), 6)

    def test_empty_input(self):
        self.assertEqual(unique_product([]), 1)

    def test_single_element_input(self):
        self.assertEqual(unique_product([5]), 5)

    def test_multiple_duplicates_input(self):
        self.assertEqual(unique_product([1, 2, 2, 3, 3, 3]), 6)

    def test_negative_numbers_input(self):
        self.assertEqual(unique_product([-1, -2, 3]), -2)

    def test_mixed_positive_negative_input(self):
        self.assertEqual(unique_product([1, -2, 3, -4]), -24)

    def test_large_numbers_input(self):
        self.assertEqual(unique_product([100, 200, 300]), 600000000)

    def test_zero_in_input(self):
        self.assertEqual(unique_product([0, 1, 2]), 0)
