import unittest
from mbpp_473_code import tuple_intersection

class TestTupleIntersection(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(tuple_intersection([(1,2), (3,4), (5,6)], [(2,1), (4,3), (6,5)]), {(1,2), (3,4), (5,6)})

    def test_empty_input(self):
        self.assertEqual(tuple_intersection([], []), set())

    def test_single_input(self):
        self.assertEqual(tuple_intersection([(1,2)], []), set())

    def test_intersection_empty(self):
        self.assertEqual(tuple_intersection([(1,2), (3,4)], []), set())

    def test_intersection_full(self):
        self.assertEqual(tuple_intersection([(1,2), (2,1)], [(2,1), (1,2)]), {(1,2), (2,1)})

    def test_duplicates(self):
        self.assertEqual(tuple_intersection([(1,2), (2,2), (3,4)], [(2,2), (4,3)]), {(1,2), (2,2), (3,4)})

    def test_order_matters(self):
        self.assertEqual(tuple_intersection([(1,2), (3,4), (5,6)], [(5,6), (3,4), (1,2)]), {(1,2), (3,4), (5,6)})

    def test_non_tuple_input(self):
        with self.assertRaises(TypeError):
            tuple_intersection([1,2,3], [4,5,6])

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            tuple_intersection({1,2,3}, [4,5,6])
