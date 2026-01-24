import unittest
from mbpp_484_code import remove_matching_tuple

class TestRemoveMatchingTuple(unittest.TestCase):

    def test_typical_case(self):
        test_list1 = [(1, 2), (3, 4), (5, 6)]
        test_list2 = [(1, 2), (3, 4)]
        expected_output = [(5, 6)]
        self.assertEqual(remove_matching_tuple(test_list1, test_list2), expected_output)

    def test_empty_list(self):
        test_list1 = []
        test_list2 = [(1, 2), (3, 4)]
        expected_output = []
        self.assertEqual(remove_matching_tuple(test_list1, test_list2), expected_output)

    def test_no_match(self):
        test_list1 = [(1, 2), (3, 4), (5, 6)]
        test_list2 = [(7, 8), (9, 10)]
        expected_output = [(1, 2), (3, 4), (5, 6)]
        self.assertEqual(remove_matching_tuple(test_list1, test_list2), expected_output)

    def test_duplicate_in_list2(self):
        test_list1 = [(1, 2), (3, 4), (5, 6), (1, 2)]
        test_list2 = [(1, 2), (3, 4)]
        expected_output = [(5, 6)]
        self.assertEqual(remove_matching_tuple(test_list1, test_list2), expected_output)

    def test_duplicate_in_list1(self):
        test_list1 = [(1, 2), (3, 4), (1, 2), (5, 6)]
        test_list2 = [(1, 2), (3, 4)]
        expected_output = [(5, 6)]
        self.assertEqual(remove_matching_tuple(test_list1, test_list2), expected_output)

    def test_same_tuple_in_both_lists(self):
        test_list1 = [(1, 2), (3, 4), (1, 2), (5, 6)]
        test_list2 = [(1, 2), (3, 4), (1, 2), (5, 6)]
        expected_output = []
        self.assertEqual(remove_matching_tuple(test_list1, test_list2), expected_output)
