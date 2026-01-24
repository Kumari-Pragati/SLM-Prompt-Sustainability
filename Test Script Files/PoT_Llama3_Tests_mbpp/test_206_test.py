import unittest
from mbpp_206_code import concatenate_elements

class TestConcatenateElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(concatenate_elements((1, 2, 3)), (3, 4, 5))

    def test_edge_case_empty_tuple(self):
        self.assertEqual(concatenate_elements(()), ())

    def test_edge_case_single_element_tuple(self):
        self.assertEqual(concatenate_elements((1,)), ())

    def test_edge_case_two_element_tuple(self):
        self.assertEqual(concatenate_elements((1, 2)), (3,))

    def test_edge_case_three_element_tuple(self):
        self.assertEqual(concatenate_elements((1, 2, 3)), (3, 4, 5))

    def test_edge_case_long_tuple(self):
        self.assertEqual(concatenate_elements((1, 2, 3, 4, 5)), (3, 4, 5, 5, 6))

    def test_edge_case_tuple_with_duplicates(self):
        self.assertEqual(concatenate_elements((1, 1, 2, 2)), (2, 3, 3, 4))

    def test_edge_case_tuple_with_negative_numbers(self):
        self.assertEqual(concatenate_elements((-1, -2, -3)), (-2, -3, -4))

    def test_edge_case_tuple_with_mixed_signs(self):
        self.assertEqual(concatenate_elements((1, -2, 3)), (1, 1, 4))
