import unittest
from mbpp_951_code import max_similar_indices

class TestMaxSimilarIndices(unittest.TestCase):

    def test_typical_case(self):
        test_list1 = [(1, 2), (3, 4), (5, 6)]
        test_list2 = [(2, 3), (4, 5), (6, 7)]
        expected_output = [(2, 3), (4, 5), (6, 7)]
        self.assertEqual(max_similar_indices(test_list1, test_list2), expected_output)

    def test_edge_case(self):
        test_list1 = [(1, 2), (3, 4), (5, 6)]
        test_list2 = [(0, 0), (0, 0), (0, 0)]
        expected_output = [(1, 2), (3, 4), (5, 6)]
        self.assertEqual(max_similar_indices(test_list1, test_list2), expected_output)

    def test_corner_case(self):
        test_list1 = [(1, 2), (3, 4), (5, 6)]
        test_list2 = [(10, 11), (12, 13), (14, 15)]
        expected_output = [(10, 11), (12, 13), (14, 15)]
        self.assertEqual(max_similar_indices(test_list1, test_list2), expected_output)

    def test_invalid_input(self):
        test_list1 = [(1, 2), (3, 4), (5, 6)]
        test_list2 = [(1, 2), (3, 'a'), (5, 6)]
        with self.assertRaises(TypeError):
            max_similar_indices(test_list1, test_list2)
