import unittest
from mbpp_473_code import tuple_intersection

class TestTupleIntersection(unittest.TestCase):

    def test_typical_case(self):
        self.assertListEqual(tuple_intersection([(1, 2), (2, 3), (3, 4)], [(2, 3), (3, 4), (4, 5)]), [(2, 3), (3, 4)])

    def test_empty_lists(self):
        self.assertListEqual(tuple_intersection([], []), [])

    def test_one_empty_list(self):
        self.assertListEqual(tuple_intersection([(1, 2)], []), [])
        self.assertListEqual(tuple_intersection([], [(1, 2)]), [])

    def test_single_tuples(self):
        self.assertListEqual(tuple_intersection([(1, 2)], [(2, 1)]), [])
        self.assertListEqual(tuple_intersection([(1, 2)], [(2, 2)]), [(1, 2)])

    def test_duplicates(self):
        self.assertListEqual(tuple_intersection([(1, 2), (1, 2)], [(2, 1), (1, 2)]), [(1, 2)])

    def test_sorted_order(self):
        self.assertListEqual(tuple_intersection([(2, 1), (1, 2)], [(1, 2), (2, 1)]), [])

    def test_negative_numbers(self):
        self.assertListEqual(tuple_intersection([(-1, 2), (2, -1)], [(-1, -2), (1, 2)]), [])

    def test_mixed_types(self):
        self.assertRaises(TypeError, tuple_intersection, [(1, 2), 'abc'], [(2, 3), 4])
