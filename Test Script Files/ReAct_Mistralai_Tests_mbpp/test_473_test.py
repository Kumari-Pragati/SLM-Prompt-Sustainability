import unittest
from mbpp_473_code import tuple_intersection

class TestTupleIntersection(unittest.TestCase):

    def test_empty_lists(self):
        self.assertListEqual([], tuple_intersection([], []))

    def test_single_element_lists(self):
        self.assertListEqual([(1, 2)], tuple_intersection([(1, 2)], []))
        self.assertListEqual([(1, 2)], tuple_intersection([], [(1, 2)]) )
        self.assertListEqual([], tuple_intersection([(1, 2)], [(3, 4)]))
        self.assertListEqual([], tuple_intersection([(3, 4)], [(1, 2)]))

    def test_equal_lists(self):
        self.assertListEqual([(1, 2), (3, 4)], tuple_intersection([(1, 2), (3, 4)], [(1, 2), (3, 4)]))

    def test_different_lengths(self):
        self.assertListEqual([], tuple_intersection([(1, 2), (3, 4)], [(5, 6)]))

    def test_duplicates(self):
        self.assertListEqual([(1, 2), (1, 2)], tuple_intersection([(1, 2), (1, 2)], [(1, 2)]))

    def test_mixed_types(self):
        self.assertRaises(TypeError, tuple_intersection, [(1, 2), 3], [(1, 2), 3])

    def test_unsorted_lists(self):
        self.assertListEqual([(1, 2)], tuple_intersection([(2, 1)], [(1, 2)]))
