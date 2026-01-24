import unittest
from mbpp_473_code import tuple_intersection

class TestTupleIntersection(unittest.TestCase):

    def test_simple_intersection(self):
        self.assertListEqual(tuple_intersection([(1, 2), (2, 3), (3, 4)], [(2, 3), (3, 4), (4, 5)]), [(2, 3), (3, 4)])
        self.assertListEqual(tuple_intersection([(0, 0), (1, 1), (2, 2)], [(0, 0), (1, 1), (2, 2)]), [(0, 0), (1, 1), (2, 2)])

    def test_empty_lists(self):
        self.assertListEqual(tuple_intersection([], []), [])
        self.assertListEqual(tuple_intersection([(1, 2)], []), [])
        self.assertListEqual(tuple_intersection([], [(1, 2)]), [])

    def test_single_element_lists(self):
        self.assertListEqual(tuple_intersection([(1, 2)], [(1, 2)]), [(1, 2)])
        self.assertListEqual(tuple_intersection([(1, 2)], [(2, 1)]), [])

    def test_different_lengths(self):
        self.assertListEqual(tuple_intersection([(1, 2), (2, 3)], [(2, 3), (3, 4)]), [(2, 3)])
        self.assertListEqual(tuple_intersection([(1, 2), (2, 3)], [(2, 3), (3, 4), (5, 6)]), [])

    def test_duplicates(self):
        self.assertListEqual(tuple_intersection([(1, 2), (1, 2), (2, 3)], [(2, 3), (3, 4)]), [(1, 2), (2, 3)])
        self.assertListEqual(tuple_intersection([(1, 2), (1, 2), (2, 3)], [(2, 3), (3, 4), (2, 3)]), [(1, 2), (2, 3)])
