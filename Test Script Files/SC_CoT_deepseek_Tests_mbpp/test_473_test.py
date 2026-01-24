import unittest
from mbpp_473_code import tuple_intersection

class TestTupleIntersection(unittest.TestCase):

    def test_typical_case(self):
        test_list1 = [(1, 2), (3, 4), (5, 6)]
        test_list2 = [(4, 3), (2, 1), (6, 5)]
        expected_output = {(1, 2), (3, 4), (5, 6)}
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

    def test_same_tuples_different_order(self):
        test_list1 = [(1, 2), (3, 4), (5, 6)]
        test_list2 = [(2, 1), (4, 3), (6, 5)]
        expected_output = {(1, 2), (3, 4), (5, 6)}
        self.assertEqual(tuple_intersection(test_list1, test_list2), expected_output)

    def test_no_intersection(self):
        test_list1 = [(1, 2), (3, 4), (5, 6)]
        test_list2 = [(7, 8), (9, 10), (11, 12)]
        expected_output = set()
        self.assertEqual(tuple_intersection(test_list1, test_list2), expected_output)

    def test_duplicate_tuples(self):
        test_list1 = [(1, 2), (3, 4), (5, 6), (1, 2)]
        test_list2 = [(2, 1), (4, 3), (6, 5), (2, 1)]
        expected_output = {(1, 2), (3, 4), (5, 6)}
        self.assertEqual(tuple_intersection(test_list1, test_list2), expected_output)
