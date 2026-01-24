import unittest
from mbpp_528_code import min_length

class TestMinLength(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(min_length([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]), (3, ['g', 'h', 'i']))

    def test_edge_case_empty_list(self):
        self.assertEqual(min_length([]), (0, None))

    def test_edge_case_single_element_list(self):
        self.assertEqual(min_length(['a']), (1, 'a'))

    def test_edge_case_all_elements_of_same_length(self):
        self.assertEqual(min_length([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]), (3, ['a', 'b', 'c']))

    def test_edge_case_min_length_is_zero(self):
        self.assertEqual(min_length([[], [], []]), (0, None))

    def test_edge_case_min_length_is_one(self):
        self.assertEqual(min_length([['a'], ['b'], ['c']]), (1, 'a'))

    def test_edge_case_min_length_is_greater_than_one(self):
        self.assertEqual(min_length([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]), (3, 'a'))

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            min_length('abc')

    def test_invalid_input_non_list_of_strings(self):
        with self.assertRaises(TypeError):
            min_length([1, 2, 3])
