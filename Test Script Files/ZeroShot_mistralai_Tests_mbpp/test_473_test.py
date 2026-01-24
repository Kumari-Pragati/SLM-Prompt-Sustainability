import unittest
from mbpp_473_code import tuple_intersection

class TestTupleIntersection(unittest.TestCase):

    def test_empty_lists(self):
        self.assertSetEqual(tuple_intersection([], []), set())

    def test_single_element_lists(self):
        self.assertSetEqual(tuple_intersection([(1, 2)], []), set())
        self.assertSetEqual(tuple_intersection([], [(1, 2)]), set())
        self.assertSetEqual(tuple_intersection([(1, 2)], [(1, 2)]), {((1, 2))})

    def test_simple_intersection(self):
        self.assertSetEqual(tuple_intersection([(1, 2), (2, 3), (3, 4)],
                                                [(2, 3), (3, 4), (4, 5)]),
                             {((2, 3), (3, 4))})

    def test_intersection_with_duplicates(self):
        self.assertSetEqual(tuple_intersection([(1, 2), (2, 3), (3, 4), (2, 3)],
                                                [(2, 3), (3, 4), (4, 5)]),
                             {((2, 3), (3, 4))})

    def test_intersection_with_different_order(self):
        self.assertSetEqual(tuple_intersection([(1, 2), (2, 3), (3, 4)],
                                                [(3, 2), (2, 1), (4, 3)]),
                             {((2, 3), (3, 2))})

    def test_intersection_with_different_types(self):
        self.assertSetEqual(tuple_intersection([(1, 2), (2, 3), (3, 4)],
                                                [(1, 'a'), (2, 'b'), (3, 'c')]),
                             set())
