import unittest
from mbpp_951_code import max_similar_indices

class TestMaxSimilarIndices(unittest.TestCase):
    def test_typical_input(self):
        test_list1 = [(1, 2), (3, 4), (5, 6)]
        test_list2 = [(1, 2), (3, 4), (5, 6)]
        self.assertEqual(max_similar_indices(test_list1, test_list2), [(1, 2), (3, 4), (5, 6)])

    def test_edge_case_empty_lists(self):
        test_list1 = []
        test_list2 = []
        self.assertEqual(max_similar_indices(test_list1, test_list2), [])

    def test_edge_case_single_element_lists(self):
        test_list1 = [(1, 2)]
        test_list2 = [(1, 2)]
        self.assertEqual(max_similar_indices(test_list1, test_list2), [(1, 2)])

    def test_edge_case_lists_of_different_lengths(self):
        test_list1 = [(1, 2), (3, 4)]
        test_list2 = [(1, 2), (3, 4), (5, 6)]
        self.assertEqual(max_similar_indices(test_list1, test_list2), [(1, 2), (3, 4)])

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            max_similar_indices("not a list", [1, 2, 3])

    def test_invalid_input_non_tuple(self):
        with self.assertRaises(TypeError):
            max_similar_indices([1, 2, 3], "not a list")
