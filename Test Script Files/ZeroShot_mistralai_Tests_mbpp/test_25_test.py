import unittest
from mbpp_25_code import find_Product

class TestFindProduct(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(find_Product([], 0), 1)

    def test_single_element(self):
        self.assertEqual(find_Product([1], 1), 1)

    def test_duplicates(self):
        self.assertEqual(find_Product([1, 1, 2], 3), 2)

    def test_multiple_unique_elements(self):
        self.assertEqual(find_Product([1, 2, 3, 4], 4), 24)

    def test_negative_numbers(self):
        self.assertEqual(find_Product([-1, -2, -3], 3), -6)

    def test_large_numbers(self):
        self.assertEqual(find_Product([1000, 2000, 3000], 3), 6000000)
