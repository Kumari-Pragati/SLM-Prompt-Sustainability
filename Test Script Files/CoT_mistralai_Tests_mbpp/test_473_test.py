import unittest
from mbpp_473_code import tuple_intersection

class TestTupleIntersection(unittest.TestCase):

    def test_empty_lists(self):
        self.assertListEqual([], tuple_intersection([], []))

    def test_single_element_lists(self):
        self.assertListEqual([(1, 2)], tuple_intersection([(1, 2)], []))
        self.assertListEqual([(1, 2)], tuple_intersection([], [(1, 2)]))
        self.assertListEqual([], tuple_intersection([(1, 2)], [(3, 4)]))
        self.assertListEqual([], tuple_intersection([(3, 4)], [(1, 2)]))

    def test_identical_lists(self):
        self.assertListEqual([(1, 2), (3, 4)], tuple_intersection([(1, 2), (3, 4)], [(1, 2), (3, 4)]))

    def test_lists_with_duplicates(self):
        self.assertListEqual([(1, 2), (3, 4)], tuple_intersection([(1, 2), (1, 2), (3, 4)], [(1, 2), (3, 4)]))

    def test_lists_with_different_order(self):
        self.assertListEqual([(1, 2), (3, 4)], tuple_intersection([(3, 4), (1, 2)], [(1, 2), (3, 4)]))

    def test_lists_with_different_types(self):
        self.assertRaises(TypeError, tuple_intersection, [(1, 2), 3], [(1, 2), (3, 4)])
        self.assertRaises(TypeError, tuple_intersection, [(1, 2), (3, 4)], [1, 2])

    def test_lists_with_non_tuples(self):
        self.assertRaises(TypeError, tuple_intersection, [(1, 2), 3], [(1, 2), [3, 4]])
        self.assertRaises(TypeError, tuple_intersection, [(1, 2), [3, 4]], [(1, 2), (3, 4)])
