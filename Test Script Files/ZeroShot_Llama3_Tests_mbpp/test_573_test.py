import unittest
from mbpp_573_code import unique_product

class TestUniqueProduct(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(unique_product([]), 1)

    def test_single_element_list(self):
        self.assertEqual(unique_product([1]), 1)

    def test_multiple_elements_list(self):
        self.assertEqual(unique_product([1, 2, 3]), 6)

    def test_negative_numbers(self):
        self.assertEqual(unique_product([-1, -2, -3]), -6)

    def test_duplicates(self):
        self.assertEqual(unique_product([1, 2, 2, 3, 3, 3]), 36)

    def test_non_integer_values(self):
        self.assertEqual(unique_product([1, 2, 3.5]), 6)

    def test_mixed_types(self):
        self.assertEqual(unique_product([1, 2, 3, 'a', 'b', 'c']), 6)
