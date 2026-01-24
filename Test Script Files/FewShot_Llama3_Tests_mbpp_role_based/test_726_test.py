import unittest
from mbpp_726_code import multiply_elements

class TestMultiplyElements(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(multiply_elements((1, 2, 3)), (2, 3, 6))

    def test_edge_case_single_element(self):
        self.assertEqual(multiply_elements((1,)), ())

    def test_edge_case_empty_tuple(self):
        self.assertEqual(multiply_elements(()), ())

    def test_edge_case_single_element_tuple(self):
        self.assertEqual(multiply_elements((1,)), ())

    def test_edge_case_tuple_with_duplicates(self):
        self.assertEqual(multiply_elements((1, 1, 2)), (1, 2, 2))

    def test_edge_case_tuple_with_negative_numbers(self):
        self.assertEqual(multiply_elements((-1, -2, -3)), (2, 2, 6))
