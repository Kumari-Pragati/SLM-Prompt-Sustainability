import unittest
from mbpp_573_code import unique_product

class TestUniqueProduct(unittest.TestCase):

    def test_empty_list(self):
        """Test unique_product on an empty list"""
        self.assertEqual(unique_product([]), 1)

    def test_single_element_list(self):
        """Test unique_product on a list with one element"""
        for num in range(1, 10):
            self.assertEqual(unique_product([num]), num)

    def test_multiple_elements(self):
        """Test unique_product on a list with multiple elements"""
        test_list = [2, 3, 4, 5]
        expected_result = 240
        self.assertEqual(unique_product(test_list), expected_result)

    def test_duplicate_elements(self):
        """Test unique_product on a list with duplicate elements"""
        test_list = [2, 2, 3, 4, 5]
        expected_result = 24
        self.assertEqual(unique_product(test_list), expected_result)

    def test_negative_numbers(self):
        """Test unique_product on a list with negative numbers"""
        test_list = [-2, -3, 4, 5]
        expected_result = -240
        self.assertEqual(unique_product(test_list), expected_result)

    def test_zero(self):
        """Test unique_product on a list with zero"""
        test_list = [0, 2, 3, 4, 5]
        self.assertEqual(unique_product(test_list), 120)
