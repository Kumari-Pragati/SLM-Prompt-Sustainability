import unittest
from mbpp_528_code import min_length

class TestMinLength(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_length([1, 2, 3, 4, 5]), (1, 1))

    def test_edge_case_empty_list(self):
        self.assertEqual(min_length([]), (0, None))

    def test_edge_case_single_element_list(self):
        self.assertEqual(min_length([1]), (1, 1))

    def test_edge_case_all_equal_length(self):
        self.assertEqual(min_length([1, 2, 3, 4, 5]), (1, 1))

    def test_edge_case_min_length_is_zero(self):
        self.assertEqual(min_length([0, 0, 0]), (0, 0))

    def test_edge_case_min_length_is_one(self):
        self.assertEqual(min_length(['a', 'b', 'c']), (1, 'a'))

    def test_edge_case_min_length_is_greater_than_one(self):
        self.assertEqual(min_length(['a', 'bc', 'cde']), (1, 'a'))

    def test_edge_case_min_length_is_greater_than_one_with_non_strings(self):
        self.assertEqual(min_length([1, 2, 3]), (1, 1))

    def test_edge_case_min_length_is_greater_than_one_with_mixed_types(self):
        self.assertEqual(min_length([1, 'a', 2, 'bc', 3]), (1, 1))
