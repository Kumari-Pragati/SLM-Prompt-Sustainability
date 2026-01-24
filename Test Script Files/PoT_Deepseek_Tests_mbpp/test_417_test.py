import unittest
from mbpp_417_code import group_tuples

class TestGroupTuples(unittest.TestCase):

    def test_typical_case(self):
        input_data = [('a', 1, 2, 3), ('b', 4, 5), ('a', 2, 3)]
        expected_output = [('a', 1, 2, 3, 2, 3), ('b', 4, 5)]
        self.assertEqual(group_tuples(input_data), expected_output)

    def test_edge_case_empty_input(self):
        self.assertEqual(group_tuples([]), [])

    def test_boundary_case_single_tuple(self):
        input_data = [('a', 1, 2, 3)]
        expected_output = [('a', 1, 2, 3)]
        self.assertEqual(group_tuples(input_data), expected_output)

    def test_corner_case_duplicate_keys(self):
        input_data = [('a', 1, 2, 3), ('a', 4, 5)]
        expected_output = [('a', 1, 2, 3, 4, 5)]
        self.assertEqual(group_tuples(input_data), expected_output)

    def test_corner_case_no_elements_in_tuples(self):
        input_data = [('a',), ('b',)]
        expected_output = [('a',), ('b',)]
        self.assertEqual(group_tuples(input_data), expected_output)
