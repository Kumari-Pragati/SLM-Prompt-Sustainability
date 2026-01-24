import unittest
from mbpp_473_code import tuple_intersection

class TestTupleIntersection(unittest.TestCase):

    def test_typical_case(self):
        test_list1 = [(1, 2), (3, 4), (5, 6)]
        test_list2 = [(4, 5), (6, 7), (8, 9)]
        expected_output = set()
        self.assertEqual(tuple_intersection(test_list1, test_list2), expected_output)

    def test_typical_case_with_duplicates(self):
        test_list1 = [(1, 2), (3, 4), (5, 6), (1, 2)]
        test_list2 = [(4, 5), (6, 7), (8, 9), (4, 5)]
        expected_output = {(1, 2), (3, 4)}
        self.assertEqual(tuple_intersection(test_list1, test_list2), expected_output)

    def test_empty_lists(self):
        test_list1 = []
        test_list2 = []
        expected_output = set()
        self.assertEqual(tuple_intersection(test_list1, test_list2), expected_output)

    def test_one_empty_list(self):
        test_list1 = []
        test_list2 = [(1, 2), (3, 4), (5, 6)]
        expected_output = set()
        self.assertEqual(tuple_intersection(test_list1, test_list2), expected_output)

    def test_same_lists(self):
        test_list1 = [(1, 2), (3, 4), (5, 6)]
        test_list2 = [(1, 2), (3, 4), (5, 6)]
        expected_output = {(1, 2), (3, 4), (5, 6)}
        self.assertEqual(tuple_intersection(test_list1, test_list2), expected_output)

    def test_single_element_lists(self):
        test_list1 = [(1, 2)]
        test_list2 = [(1, 2)]
        expected_output = {(1, 2)}
        self.assertEqual(tuple_intersection(test_list1, test_list2), expected_output)

    def test_unsorted_tuples(self):
        test_list1 = [(2, 1), (4, 3)]
        test_list2 = [(1, 2), (3, 4)]
        expected_output = {(1, 2), (3, 4)}
        self.assertEqual(tuple_intersection(test_list1, test_list2), expected_output)
