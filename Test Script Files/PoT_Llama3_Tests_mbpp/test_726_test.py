import unittest
from mbpp_726_code import multiply_elements

class TestMultiplyElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(multiply_elements((1, 2, 3)), (2, 3, 6))

    def test_edge_case_empty_tuple(self):
        self.assertEqual(multiply_elements(()), ())

    def test_edge_case_single_element_tuple(self):
        self.assertEqual(multiply_elements((1,)), ())

    def test_edge_case_two_element_tuple(self):
        self.assertEqual(multiply_elements((1, 2)), ())

    def test_edge_case_three_element_tuple(self):
        self.assertEqual(multiply_elements((1, 2, 3)), (2, 6))

    def test_edge_case_tuple_with_duplicates(self):
        self.assertEqual(multiply_elements((1, 2, 2, 3)), (2, 6, 6))

    def test_edge_case_tuple_with_negative_numbers(self):
        self.assertEqual(multiply_elements((-1, 2, 3)), (-2, 6))

    def test_edge_case_tuple_with_zero(self):
        self.assertEqual(multiply_elements((0, 1, 2)), (0, 0, 0))

    def test_edge_case_tuple_with_negative_and_positive_numbers(self):
        self.assertEqual(multiply_elements((-1, 2, 3)), (-2, 6))
