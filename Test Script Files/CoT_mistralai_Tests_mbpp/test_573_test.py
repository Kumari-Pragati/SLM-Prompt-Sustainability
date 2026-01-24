import unittest
from mbpp_573_code import unique_product

class TestUniqueProduct(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(unique_product([]), 1)

    def test_single_element_list(self):
        for num in range(1, 10):
            self.assertEqual(unique_product([num]), num)

    def test_multiple_elements(self):
        test_list = [2, 3, 5, 7]
        self.assertEqual(unique_product(test_list), 2 * 3 * 5 * 7)

    def test_duplicate_elements(self):
        test_list = [2, 3, 5, 2, 7]
        self.assertEqual(unique_product(test_list), 2 * 3 * 5 * 7)

    def test_negative_numbers(self):
        test_list = [-2, -3, 5, 7]
        self.assertEqual(unique_product(test_list), (-2) * (-3) * 5 * 7)

    def test_zero(self):
        self.assertEqual(unique_product([0]), 0)
