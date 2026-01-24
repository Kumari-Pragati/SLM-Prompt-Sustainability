import unittest
from mbpp_922_code import max_product

class TestMaxProduct(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_product([]))

    def test_single_element_list(self):
        self.assertIsNone(max_product([1]))

    def test_two_elements_list(self):
        self.assertEqual(max_product([1, 2]), (1, 2))
        self.assertEqual(max_product([2, 1]), (1, 2))

    def test_positive_numbers_list(self):
        self.assertEqual(max_product([1, 2, 3, 4, 5]), (1, 5))
        self.assertEqual(max_product([5, 4, 3, 2, 1]), (5, 1))

    def test_negative_numbers_list(self):
        self.assertEqual(max_product([-1, -2, -3, -4, -5]), (-1, -5))
        self.assertEqual(max_product([-5, -4, -3, -2, -1]), (-5, -1))

    def test_mixed_numbers_list(self):
        self.assertEqual(max_product([1, -2, 3, -4, 5]), (1, 5))
        self.assertEqual(max_product([-1, 2, -3, 4, -5]), (-1, -5))

    def test_zero_in_list(self):
        self.assertEqual(max_product([0, 1, 2, 3, 4]), (0, 4))
        self.assertEqual(max_product([4, 3, 2, 1, 0]), (4, 0))
