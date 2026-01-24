import unittest
from mbpp_528_code import min_length

class TestMinLength(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_length([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), (3, [1, 2, 3]))

    def test_edge_case_empty_list(self):
        self.assertEqual(min_length([]), (0, []))

    def test_edge_case_single_element_list(self):
        self.assertEqual(min_length([[1, 2, 3]]), (3, [1, 2, 3]))

    def test_edge_case_all_elements_of_same_length(self):
        self.assertEqual(min_length([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), (3, [1, 2, 3]))

    def test_edge_case_min_length_is_zero(self):
        self.assertEqual(min_length([[]]), (0, []))

    def test_edge_case_min_length_is_one(self):
        self.assertEqual(min_length([['a']]), (1, ['a']))

    def test_edge_case_min_length_is_greater_than_one(self):
        self.assertEqual(min_length([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]), (3, ['a', 'b', 'c']))
