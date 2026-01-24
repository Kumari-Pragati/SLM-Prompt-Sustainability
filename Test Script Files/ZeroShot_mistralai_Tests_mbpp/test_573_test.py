import unittest
from mbpp_573_code import unique_product

class TestUniqueProduct(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(unique_product([]), 1)

    def test_single_element_list(self):
        self.assertEqual(unique_product([1]), 1)

    def test_list_with_duplicates(self):
        self.assertEqual(unique_product([1, 1, 2]), 2)

    def test_list_with_negative_numbers(self):
        self.assertEqual(unique_product([-1, -2, -3]), abs(unique_product([1, 2, 3])))

    def test_list_with_zero(self):
        self.assertEqual(unique_product([0, 1, 2]), 2)

    def test_large_list(self):
        self.assertEqual(unique_product(list(range(100))), 9648000)
