import unittest
from mbpp_922_code import max_product

class TestMaxProduct(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(max_product([]))

    def test_single_element(self):
        self.assertIsNone(max_product([1]))

    def test_two_elements(self):
        self.assertEqual(max_product([1, 2]), (1, 2))
        self.assertEqual(max_product([2, 1]), (2, 1))

    def test_negative_numbers(self):
        self.assertEqual(max_product([-1, -2]), (-1, -2))
        self.assertEqual(max_product([-2, -1]), (-2, -1))

    def test_positive_and_negative_numbers(self):
        self.assertEqual(max_product([1, -2, 3, -4]), (1, -4))
        self.assertEqual(max_product([-1, 2, -3, 4]), (-1, 4))

    def test_large_numbers(self):
        self.assertEqual(max_product([1000000, 2000000]), (1000000, 2000000))
        self.assertEqual(max_product([2000000, 1000000]), (2000000, 1000000))
