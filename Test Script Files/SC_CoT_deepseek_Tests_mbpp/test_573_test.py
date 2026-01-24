import unittest
from mbpp_573_code import unique_product

class TestUniqueProduct(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(unique_product([1, 2, 3, 4]), 24)

    def test_single_element(self):
        self.assertEqual(unique_product([5]), 5)

    def test_empty_list(self):
        self.assertEqual(unique_product([]), 1)

    def test_duplicate_elements(self):
        self.assertEqual(unique_product([2, 2, 2]), 4)

    def test_negative_numbers(self):
        self.assertEqual(unique_product([-1, -2, -3]), -6)

    def test_zero(self):
        self.assertEqual(unique_product([0, 2, 3]), 0)

    def test_large_numbers(self):
        self.assertEqual(unique_product([10**6, 10**6]), 10**12)

    def test_non_integer_elements(self):
        with self.assertRaises(TypeError):
            unique_product([1, 2, '3'])

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            unique_product('1,2,3')
