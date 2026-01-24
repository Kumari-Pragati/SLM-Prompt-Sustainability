import unittest
from mbpp_75_code import find_tuples

class TestFindTuples(unittest.TestCase):

    def test_simple_valid_input(self):
        self.assertEqual(find_tuples([(4, 8, 12), (3, 6, 9)], 2), '[(4, 8, 12)]')

    def test_edge_case_empty_list(self):
        self.assertEqual(find_tuples([], 2), '[]')

    def test_boundary_case_single_tuple(self):
        self.assertEqual(find_tuples([(4, 8, 12)], 2), '[(4, 8, 12)]')

    def test_complex_case_mixed_valid_and_invalid_tuples(self):
        self.assertEqual(find_tuples([(4, 8, 12), (3, 6, 9), (5, 10)], 2), '[(4, 8, 12)]')

    def test_edge_case_tuple_with_non_integer_elements(self):
        self.assertEqual(find_tuples([(4, 8, 12), ('3', 6, 9)], 2), '[(4, 8, 12)]')

    def test_boundary_case_tuple_with_zero(self):
        self.assertEqual(find_tuples([(4, 8, 12), (0, 6, 9)], 2), '[(4, 8, 12)]')

    def test_complex_case_tuple_with_negative_numbers(self):
        self.assertEqual(find_tuples([(4, 8, -12), (-3, 6, 9)], 2), '[(4, 8, -12)]')
