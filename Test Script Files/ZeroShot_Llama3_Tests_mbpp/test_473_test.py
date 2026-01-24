import unittest
from mbpp_473_code import tuple_intersection

class TestTupleIntersection(unittest.TestCase):

    def test_empty_lists(self):
        self.assertEqual(tuple_intersection([], []), ())

    def test_single_element_lists(self):
        self.assertEqual(tuple_intersection([(1,)], [(1,)]), ((1,),))
        self.assertEqual(tuple_intersection([(1,)], [(2,)]), ((1,),))
        self.assertEqual(tuple_intersection([(1,)], []), ())
        self.assertEqual(tuple_intersection([()], [(1,)]), ())

    def test_multiple_element_lists(self):
        self.assertEqual(tuple_intersection([(1, 2), (2, 1)], [(1, 2), (2, 1)]), ((1, 2),))
        self.assertEqual(tuple_intersection([(1, 2), (2, 1)], [(1, 2)]), ((1, 2),))
        self.assertEqual(tuple_intersection([(1, 2), (2, 1)], [(3, 4)]), ())
        self.assertEqual(tuple_intersection([(1, 2), (2, 1), (3, 4)], [(1, 2), (2, 1)]), ((1, 2),))

    def test_duplicates(self):
        self.assertEqual(tuple_intersection([(1, 1), (1, 2), (2, 1)], [(1, 1), (1, 2), (2, 1)]), ((1, 1),))
        self.assertEqual(tuple_intersection([(1, 1), (1, 2), (2, 1)], [(1, 1), (1, 2)]), ((1, 1),))
