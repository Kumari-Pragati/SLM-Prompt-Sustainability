import unittest
from mbpp_922_code import max_product

class TestMaxProduct(unittest.TestCase):
    def test_single_element_array(self):
        self.assertIsNone(max_product([1]))

    def test_two_element_array(self):
        self.assertEqual(max_product([1, 2]), (1, 2))

    def test_three_element_array(self):
        self.assertEqual(max_product([1, 2, 3]), (1, 2))

    def test_four_element_array(self):
        self.assertEqual(max_product([1, 2, 3, 4]), (1, 2))

    def test_five_element_array(self):
        self.assertEqual(max_product([1, 2, 3, 4, 5]), (1, 2))

    def test_negative_numbers(self):
        self.assertEqual(max_product([-1, -2, -3, -4, -5]), (-1, -2))

    def test_positive_numbers(self):
        self.assertEqual(max_product([1, 2, 3, 4, 5]), (1, 2))

    def test_mixed_numbers(self):
        self.assertEqual(max_product([-1, 2, 3, 4, -5]), (-1, 2))

    def test_empty_array(self):
        with self.assertRaises(IndexError):
            max_product([])

    def test_array_with_one_element_and_rest_zero(self):
        self.assertIsNone(max_product([1, 0, 0, 0]))
