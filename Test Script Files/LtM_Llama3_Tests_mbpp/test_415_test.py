import unittest
from mbpp_415_code import max_Product

class TestMaxProduct(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(max_Product([]), ("No pairs exists"))

    def test_single_element_array(self):
        self.assertEqual(max_Product([1]), ("No pairs exists"))

    def test_two_elements_array(self):
        self.assertEqual(max_Product([1, 2]), (1, 2))

    def test_three_elements_array(self):
        self.assertEqual(max_Product([1, 2, 3]), (1, 2))

    def test_max_product_at_first_two_elements(self):
        self.assertEqual(max_Product([3, 2, 1]), (3, 2))

    def test_max_product_at_last_two_elements(self):
        self.assertEqual(max_Product([1, 2, 3]), (1, 2))

    def test_max_product_at_middle_two_elements(self):
        self.assertEqual(max_Product([1, 2, 3, 4]), (2, 3))

    def test_max_product_at_first_and_last_elements(self):
        self.assertEqual(max_Product([1, 2, 3, 4, 5]), (1, 5))

    def test_max_product_at_first_and_middle_elements(self):
        self.assertEqual(max_Product([1, 2, 3, 4, 5, 6]), (1, 4))

    def test_max_product_at_last_and_middle_elements(self):
        self.assertEqual(max_Product([1, 2, 3, 4, 5, 6]), (4, 5))

    def test_max_product_at_first_and_last_elements_with_negative_numbers(self):
        self.assertEqual(max_Product([-1, -2, -3, -4, -5, -6]), (-1, -6))

    def test_max_product_at_first_and_middle_elements_with_negative_numbers(self):
        self.assertEqual(max_Product([-1, -2, -3, -4, -5, -6]), (-1, -4))

    def test_max_product_at_last_and_middle_elements_with_negative_numbers(self):
        self.assertEqual(max_Product([-1, -2, -3, -4, -5, -6]), (-4, -5))
