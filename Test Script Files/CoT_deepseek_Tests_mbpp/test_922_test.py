import unittest
from mbpp_922_code import max_product

class TestMaxProduct(unittest.TestCase):

    def test_single_element(self):
        self.assertIsNone(max_product([1]))

    def test_two_elements(self):
        self.assertEqual(max_product([1, 2]), (1, 2))
        self.assertEqual(max_product([-1, -2]), (-1, -2))
        self.assertEqual(max_product([-1, 2]), (-1, 2))

    def test_multiple_elements(self):
        self.assertEqual(max_product([1, 2, 3, 4]), (2, 4))
        self.assertEqual(max_product([-1, -2, -3, -4]), (-2, -4))
        self.assertEqual(max_product([-1, 2, 3, -4]), (3, -4))
        self.assertEqual(max_product([1, 2, 3, 4, 5]), (2, 4))

    def test_duplicate_elements(self):
        self.assertEqual(max_product([1, 1, 1, 1]), (1, 1))
        self.assertEqual(max_product([-1, -1, -1, -1]), (-1, -1))

    def test_negative_elements(self):
        self.assertEqual(max_product([-1, -2, -3, -4]), (-2, -4))

    def test_empty_list(self):
        self.assertIsNone(max_product([]))
