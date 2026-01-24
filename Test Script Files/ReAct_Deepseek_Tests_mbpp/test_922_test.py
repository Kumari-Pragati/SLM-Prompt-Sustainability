import unittest
from mbpp_922_code import max_product

class TestMaxProduct(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_product([1, 2, 3, 4]), (3, 4))

    def test_single_element(self):
        self.assertIsNone(max_product([1]))

    def test_empty_list(self):
        self.assertIsNone(max_product([]))

    def test_negative_numbers(self):
        self.assertEqual(max_product([-1, -2, -3, -4]), (-1, -2))

    def test_zero_in_list(self):
        self.assertEqual(max_product([0, 1, 2, 3]), (0, 1))

    def test_duplicate_elements(self):
        self.assertEqual(max_product([1, 2, 2, 3]), (2, 2))

    def test_large_numbers(self):
        self.assertEqual(max_product([1000, 2000, 3000, 4000]), (2000, 3000))

    def test_same_elements(self):
        self.assertEqual(max_product([5, 5, 5, 5]), (5, 5))
