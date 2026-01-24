import unittest
from mbpp_573_code import unique_product

class TestUniqueProduct(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(unique_product([1, 2, 3, 4, 5]), 120)

    def test_edge_case_empty_list(self):
        self.assertEqual(unique_product([]), 1)

    def test_edge_case_single_element_list(self):
        self.assertEqual(unique_product([1]), 1)

    def test_edge_case_duplicates(self):
        self.assertEqual(unique_product([1, 2, 2, 3, 3, 3]), 6)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(unique_product([-1, -2, 3, 4, 5]), -120)

    def test_edge_case_zero(self):
        self.assertEqual(unique_product([0, 1, 2, 3, 4]), 0)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            unique_product("hello")

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            unique_product([1, 2, "hello"])
