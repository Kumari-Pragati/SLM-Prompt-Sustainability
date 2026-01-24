import unittest
from mbpp_473_code import tuple_intersection

class TestTupleIntersection(unittest.TestCase):
    def test_empty_lists(self):
        self.assertEqual(tuple_intersection([], []), ())

    def test_single_element_lists(self):
        self.assertEqual(tuple_intersection([(1,)], [(1,)]), ((1,),))
        self.assertEqual(tuple_intersection([(1,)], [(2,)]), ())
        self.assertEqual(tuple_intersection([(1,)], []), ())
        self.assertEqual(tuple_intersection([], [(1,)]), ())

    def test_multiple_element_lists(self):
        self.assertEqual(tuple_intersection([(1, 2), (2, 3)], [(2, 3), (3, 4)]), ((2, 3),))
        self.assertEqual(tuple_intersection([(1, 2), (2, 3), (3, 4)], [(1, 2), (2, 3), (3, 4)]), ((1, 2), (2, 3), (3, 4)))
        self.assertEqual(tuple_intersection([(1, 2), (2, 3), (3, 4)], [(1, 2), (2, 3)]), ((1, 2), (2, 3)))
        self.assertEqual(tuple_intersection([(1, 2), (2, 3), (3, 4)], [(1, 2), (2, 3), (3, 4), (4, 5)]), ((1, 2), (2, 3), (3, 4)))
