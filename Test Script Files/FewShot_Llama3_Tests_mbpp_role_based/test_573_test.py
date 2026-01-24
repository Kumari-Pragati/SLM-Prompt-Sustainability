import unittest
from mbpp_573_code import unique_product

class TestUniqueProduct(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(unique_product([]), 1)

    def test_single_element_list(self):
        self.assertEqual(unique_product([1]), 1)

    def test_multiple_elements_list(self):
        self.assertEqual(unique_product([1, 2, 3]), 6)

    def test_duplicates_in_list(self):
        self.assertEqual(unique_product([1, 2, 2, 3]), 6)

    def test_negative_numbers(self):
        self.assertEqual(unique_product([-1, -2, 3]), -2)

    def test_zero_in_list(self):
        self.assertEqual(unique_product([0, 1, 2]), 0)

    def test_all_negative_numbers(self):
        self.assertEqual(unique_product([-1, -2, -3]), -6)
