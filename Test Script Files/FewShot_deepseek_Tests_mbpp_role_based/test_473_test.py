import unittest
from mbpp_473_code import tuple_intersection

class TestTupleIntersection(unittest.TestCase):
    def test_typical_case(self):
        test_list1 = [(1, 2), (3, 4), (5, 6)]
        test_list2 = [(4, 5), (6, 7), (8, 9)]
        self.assertEqual(tuple_intersection(test_list1, test_list2), {(4, 5), (6, 7)})

    def test_empty_lists(self):
        test_list1 = []
        test_list2 = []
        self.assertEqual(tuple_intersection(test_list1, test_list2), set())

    def test_one_empty_list(self):
        test_list1 = [(1, 2), (3, 4), (5, 6)]
        test_list2 = []
        self.assertEqual(tuple_intersection(test_list1, test_list2), set())

    def test_duplicate_tuples(self):
        test_list1 = [(1, 2), (3, 4), (5, 6), (1, 2)]
        test_list2 = [(1, 2), (3, 4), (5, 6), (1, 2)]
        self.assertEqual(tuple_intersection(test_list1, test_list2), {(1, 2), (3, 4), (5, 6)})

    def test_same_tuples(self):
        test_list1 = [(1, 2), (3, 4), (5, 6)]
        test_list2 = [(1, 2), (3, 4), (5, 6)]
        self.assertEqual(tuple_intersection(test_list1, test_list2), {(1, 2), (3, 4), (5, 6)})

    def test_unordered_tuples(self):
        test_list1 = [(2, 1), (4, 3), (6, 5)]
        test_list2 = [(1, 2), (3, 4), (5, 6)]
        self.assertEqual(tuple_intersection(test_list1, test_list2), {(1, 2), (3, 4), (5, 6)})
