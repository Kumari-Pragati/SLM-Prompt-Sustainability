import unittest
from mbpp_484_code import remove_matching_tuple

class TestRemoveMatchingTuple(unittest.TestCase):

    def test_remove_matching_tuple(self):
        test_list1 = [(1, 2), (2, 3), (3, 4)]
        test_list2 = [(1, 2), (3, 4)]
        result = remove_matching_tuple(test_list1, test_list2)
        self.assertEqual(result, [(2, 3)])

    def test_remove_matching_tuple_empty_list(self):
        test_list1 = []
        test_list2 = []
        result = remove_matching_tuple(test_list1, test_list2)
        self.assertEqual(result, [])

    def test_remove_matching_tuple_empty_list1(self):
        test_list1 = []
        test_list2 = [(1, 2), (3, 4)]
        result = remove_matching_tuple(test_list1, test_list2)
        self.assertEqual(result, [])

    def test_remove_matching_tuple_empty_list2(self):
        test_list1 = [(1, 2), (3, 4)]
        test_list2 = []
        result = remove_matching_tuple(test_list1, test_list2)
        self.assertEqual(result, test_list1)

    def test_remove_matching_tuple_no_match(self):
        test_list1 = [(1, 2), (2, 3), (3, 4)]
        test_list2 = []
        result = remove_matching_tuple(test_list1, test_list2)
        self.assertEqual(result, test_list1)
