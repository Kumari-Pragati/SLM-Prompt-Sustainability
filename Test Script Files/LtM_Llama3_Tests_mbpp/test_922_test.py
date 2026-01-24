import unittest
from mbpp_922_code import max_product

class TestMaxProduct(unittest.TestCase):
    def test_empty_input(self):
        self.assertIsNone(max_product([]))

    def test_single_element_input(self):
        self.assertIsNone(max_product([1]))

    def test_two_element_input(self):
        self.assertEqual(max_product([1, 2]), (1, 2))

    def test_three_element_input(self):
        self.assertEqual(max_product([1, 2, 3]), (1, 2))

    def test_max_product_at_first_two_elements(self):
        self.assertEqual(max_product([3, 2, 1, 4]), (3, 2))

    def test_max_product_at_last_two_elements(self):
        self.assertEqual(max_product([1, 2, 3, 4]), (3, 4))

    def test_max_product_at_middle_two_elements(self):
        self.assertEqual(max_product([1, 2, 3, 4, 5]), (3, 4))

    def test_max_product_at_first_and_last_elements(self):
        self.assertEqual(max_product([1, 2, 3, 4, 5]), (1, 5))

    def test_max_product_at_first_and_middle_elements(self):
        self.assertEqual(max_product([1, 2, 3, 4, 5]), (1, 4))

    def test_max_product_at_last_and_middle_elements(self):
        self.assertEqual(max_product([1, 2, 3, 4, 5]), (4, 3))

    def test_max_product_at_first_and_last_elements_with_duplicates(self):
        self.assertEqual(max_product([1, 2, 2, 3, 4, 5]), (1, 5))

    def test_max_product_at_first_and_middle_elements_with_duplicates(self):
        self.assertEqual(max_product([1, 2, 2, 3, 4, 5]), (1, 4))

    def test_max_product_at_last_and_middle_elements_with_duplicates(self):
        self.assertEqual(max_product([1, 2, 2, 3, 4, 5]), (4, 3))
