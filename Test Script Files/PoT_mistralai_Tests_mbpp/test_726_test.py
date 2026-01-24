import unittest
from mbpp_726_code import multiply_elements

class TestMultiplyElements(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(multiply_elements((1, 2, 3, 4)), (2, 3, 6))

    def test_edge_case_empty(self):
        self.assertEqual(multiply_elements(()), ())

    def test_edge_case_single_element(self):
        self.assertEqual(multiply_elements((1,)), ())

    def test_edge_case_single_element_end(self):
        self.assertEqual(multiply_elements((1,)), (None,))

    def test_boundary_case_zero(self):
        self.assertEqual(multiply_elements((0, 1, 2)), (0, 0, 2))

    def test_boundary_case_negative(self):
        self.assertEqual(multiply_elements((-1, 1, 2)), (-1, -1, 2))
