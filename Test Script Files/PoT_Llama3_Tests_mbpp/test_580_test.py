import unittest
from mbpp_580_code import extract_even

class TestExtractEven(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(extract_even((1, 2, 3, 4, 5)), (2, 4))

    def test_edge_case_empty_tuple(self):
        self.assertEqual(extract_even(()), ())

    def test_edge_case_single_element(self):
        self.assertEqual(extract_even((1,)), (1,))

    def test_edge_case_single_even_element(self):
        self.assertEqual(extract_even((2,)), (2,))

    def test_edge_case_single_odd_element(self):
        self.assertEqual(extract_even((3,)), ())

    def test_edge_case_nested_tuples(self):
        self.assertEqual(extract_even(((1, 2), 3, 4)), (2,))

    def test_edge_case_nested_tuples_with_even_elements(self):
        self.assertEqual(extract_even(((2, 4), 3, 5)), (2, 4))

    def test_edge_case_nested_tuples_with_odd_elements(self):
        self.assertEqual(extract_even(((1, 3), 2, 4)), (2))

    def test_edge_case_tuple_of_tuples(self):
        self.assertEqual(extract_even(((1, 2), (3, 4), (5, 6))), (2, 4))

    def test_edge_case_tuple_of_tuples_with_even_elements(self):
        self.assertEqual(extract_even(((2, 4), (3, 6), (5, 8))), (2, 4, 6, 8))

    def test_edge_case_tuple_of_tuples_with_odd_elements(self):
        self.assertEqual(extract_even(((1, 3), (2, 4), (5, 7))), (2, 4))
