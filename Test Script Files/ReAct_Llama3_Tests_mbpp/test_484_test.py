import unittest
from mbpp_484_code import remove_matching_tuple

class TestRemoveMatchingTuple(unittest.TestCase):

    def test_typical_case(self):
        test_list1 = [(1, 2), (3, 4), (5, 6)]
        test_list2 = [(1, 2), (3, 4)]
        result = remove_matching_tuple(test_list1, test_list2)
        self.assertEqual(result, [(5, 6)])

    def test_edge_case_empty_list1(self):
        test_list1 = []
        test_list2 = [(1, 2), (3, 4)]
        result = remove_matching_tuple(test_list1, test_list2)
        self.assertEqual(result, [])

    def test_edge_case_empty_list2(self):
        test_list1 = [(1, 2), (3, 4)]
        test_list2 = []
        result = remove_matching_tuple(test_list1, test_list2)
        self.assertEqual(result, test_list1)

    def test_edge_case_list1_empty_list2(self):
        test_list1 = [(1, 2), (3, 4)]
        test_list2 = []
        result = remove_matching_tuple(test_list1, test_list2)
        self.assertEqual(result, test_list1)

    def test_edge_case_list2_empty_list1(self):
        test_list1 = []
        test_list2 = [(1, 2), (3, 4)]
        result = remove_matching_tuple(test_list1, test_list2)
        self.assertEqual(result, [])

    def test_edge_case_list1_empty_list2_empty(self):
        test_list1 = []
        test_list2 = []
        result = remove_matching_tuple(test_list1, test_list2)
        self.assertEqual(result, [])

    def test_error_case_non_list_input(self):
        test_list1 = [(1, 2), (3, 4)]
        test_list2 = "not a list"
        with self.assertRaises(TypeError):
            remove_matching_tuple(test_list1, test_list2)

    def test_error_case_non_list_input2(self):
        test_list1 = "not a list"
        test_list2 = [(1, 2), (3, 4)]
        with self.assertRaises(TypeError):
            remove_matching_tuple(test_list1, test_list2)
