import unittest
from mbpp_484_code import remove_matching_tuple

class TestRemoveMatchingTuple(unittest.TestCase):

    def test_typical_case(self):
        test_list1 = [(1, 2), (3, 4), (5, 6)]
        test_list2 = [(1, 2), (3, 4)]
        self.assertEqual(remove_matching_tuple(test_list1, test_list2), [(5, 6)])

    def test_empty_lists(self):
        test_list1 = []
        test_list2 = []
        self.assertEqual(remove_matching_tuple(test_list1, test_list2), [])

    def test_all_match(self):
        test_list1 = [(1, 2), (3, 4), (5, 6)]
        test_list2 = [(1, 2), (3, 4), (5, 6)]
        self.assertEqual(remove_matching_tuple(test_list1, test_list2), [])

    def test_no_match(self):
        test_list1 = [(1, 2), (3, 4), (5, 6)]
        test_list2 = [(7, 8), (9, 10)]
        self.assertEqual(remove_matching_tuple(test_list1, test_list2), [(1, 2), (3, 4), (5, 6)])

    def test_duplicate_in_list2(self):
        test_list1 = [(1, 2), (3, 4), (5, 6)]
        test_list2 = [(1, 2), (1, 2)]
        self.assertEqual(remove_matching_tuple(test_list1, test_list2), [(3, 4), (5, 6)])
