import unittest
from mbpp_473_code import tuple_intersection

class TestTupleIntersection(unittest.TestCase):

    def test_typical_case(self):
        test_list1 = [(1, 2), (3, 4), (5, 6)]
        test_list2 = [(4, 3), (2, 1), (6, 5)]
        self.assertEqual(tuple_intersection(test_list1, test_list2), set([(1, 2), (3, 4), (5, 6)]))

    def test_empty_lists(self):
        test_list1 = []
        test_list2 = []
        self.assertEqual(tuple_intersection(test_list1, test_list2), set())

    def test_one_empty_list(self):
        test_list1 = [(1, 2), (3, 4), (5, 6)]
        test_list2 = []
        self.assertEqual(tuple_intersection(test_list1, test_list2), set())

    def test_duplicate_tuples(self):
        test_list1 = [(1, 2), (3, 4), (1, 2)]
        test_list2 = [(2, 1), (4, 3), (2, 1)]
        self.assertEqual(tuple_intersection(test_list1, test_list2), set([(1, 2), (2, 1), (3, 4), (4, 3)]))

    def test_unsorted_tuples(self):
        test_list1 = [(2, 1), (4, 3)]
        test_list2 = [(1, 2), (3, 4)]
        self.assertEqual(tuple_intersection(test_list1, test_list2), set([(1, 2), (2, 1), (3, 4), (4, 3)]))
