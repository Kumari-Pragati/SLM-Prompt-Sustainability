import unittest
from mbpp_951_code import max_similar_indices

class TestMaxSimilarIndices(unittest.TestCase):

    def test_typical_case(self):
        test_list1 = [(1, 2), (3, 4), (5, 6)]
        test_list2 = [(2, 3), (4, 5), (6, 7)]
        expected_output = [(2, 3), (4, 5), (6, 7)]
        self.assertEqual(max_similar_indices(test_list1, test_list2), expected_output)

    def test_empty_lists(self):
        test_list1 = []
        test_list2 = []
        expected_output = []
        self.assertEqual(max_similar_indices(test_list1, test_list2), expected_output)

    def test_one_empty_list(self):
        test_list1 = [(1, 2), (3, 4), (5, 6)]
        test_list2 = []
        expected_output = []
        self.assertEqual(max_similar_indices(test_list1, test_list2), expected_output)

    def test_different_lengths(self):
        test_list1 = [(1, 2), (3, 4)]
        test_list2 = [(2, 3), (4, 5), (6, 7)]
        expected_output = [(2, 3), (4, 5)]
        self.assertEqual(max_similar_indices(test_list1, test_list2), expected_output)

    def test_negative_numbers(self):
        test_list1 = [(-1, -2), (-3, -4), (-5, -6)]
        test_list2 = [(-2, -3), (-4, -5), (-6, -7)]
        expected_output = [(-1, -2), (-3, -4), (-5, -6)]
        self.assertEqual(max_similar_indices(test_list1, test_list2), expected_output)
