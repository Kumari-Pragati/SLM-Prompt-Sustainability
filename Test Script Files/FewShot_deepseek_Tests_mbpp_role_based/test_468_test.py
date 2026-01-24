import unittest
from mbpp_468_code import max_product

class TestMaxProduct(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(max_product([1, 2, 3, 4, 5], 5), 60)

    def test_edge_case_single_element(self):
        self.assertEqual(max_product([5], 1), 5)

    def test_edge_case_negative_elements(self):
        self.assertEqual(max_product([-1, -2, -3, -4, -5], 5), -6)

    def test_boundary_case_empty_array(self):
        self.assertEqual(max_product([], 0), 0)

    def test_boundary_case_one_positive_one_negative(self):
        self.assertEqual(max_product([-1, 2], 2), 2)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            max_product("not an array", 0)
