import unittest
from mbpp_951_code import max_similar_indices

class TestMaxSimilarIndices(unittest.TestCase):

    def test_typical_inputs(self):
        test_list1 = [(1, 2), (3, 4), (5, 6)]
        test_list2 = [(2, 3), (4, 5), (6, 7)]
        self.assertEqual(max_similar_indices(test_list1, test_list2), [(2, 3), (4, 5), (6, 7)])

    def test_edge_cases(self):
        test_list1 = [(1, 2), (3, 4)]
        test_list2 = [(2, 3), (4, 5)]
        self.assertEqual(max_similar_indices(test_list1, test_list2), [(2, 3), (4, 4)])

    def test_empty_lists(self):
        test_list1 = []
        test_list2 = [(2, 3), (4, 5)]
        self.assertEqual(max_similar_indices(test_list1, test_list2), [])

    def test_single_element_lists(self):
        test_list1 = [(1, 2)]
        test_list2 = [(2, 3)]
        self.assertEqual(max_similar_indices(test_list1, test_list2), [(2, 3)])

    def test_lists_of_different_lengths(self):
        test_list1 = [(1, 2), (3, 4)]
        test_list2 = [(2, 3), (4, 5), (6, 7)]
        self.assertEqual(max_similar_indices(test_list1, test_list2), [(2, 3), (4, 4)])

    def test_invalid_input_types(self):
        test_list1 = [(1, 2)]
        test_list2 = 'invalid input'
        with self.assertRaises(TypeError):
            max_similar_indices(test_list1, test_list2)

    def test_invalid_input_types2(self):
        test_list1 = 'invalid input'
        test_list2 = [(2, 3)]
        with self.assertRaises(TypeError):
            max_similar_indices(test_list1, test_list2)
