import unittest
from mbpp_726_code import multiply_elements

class TestMultiplyElements(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(multiply_elements((1, 2, 3, 4)), (2, 6, 12))

    def test_edge_case_single_element(self):
        self.assertEqual(multiply_elements((1,)), ())

    def test_edge_case_empty_list(self):
        self.assertEqual(multiply_elements(()), ())

    def test_edge_case_single_element_on_both_sides(self):
        self.assertEqual(multiply_elements((1, 1)), ())

    def test_boundary_case_zero(self):
        self.assertEqual(multiply_elements((0, 1, 2)), (0, 0, 0))

    def test_boundary_case_negative_numbers(self):
        self.assertEqual(multiply_elements((-1, -2, -3)), (1, 4, 9))
