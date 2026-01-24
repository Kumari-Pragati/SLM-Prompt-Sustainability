import unittest
from mbpp_922_code import max_product

class TestMaxProduct(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(max_product([1, 2, 3, 4]), (3, 4))

    def test_edge_case_single_element(self):
        self.assertEqual(max_product([1]), None)

    def test_edge_case_two_elements(self):
        self.assertEqual(max_product([1, 2]), (1, 2))

    def test_boundary_case_negative_numbers(self):
        self.assertEqual(max_product([-1, -2, -3, -4]), (-1, -2))

    def test_boundary_case_positive_and_negative_numbers(self):
        self.assertEqual(max_product([-1, 2, 3, 4]), (4, 3))

    def test_invalid_input_empty_list(self):
        self.assertEqual(max_product([]), None)

    def test_invalid_input_non_integer_elements(self):
        with self.assertRaises(TypeError):
            max_product([1, '2', 3, 4])
