import unittest
from mbpp_473_code import tuple_intersection

class TestTupleIntersection(unittest.TestCase):

    def test_simple_intersection(self):
        self.assertEqual(tuple_intersection([(1, 2), (3, 4)], [(2, 1), (4, 3)]), {(1, 2), (3, 4)})

    def test_empty_lists(self):
        self.assertEqual(tuple_intersection([], []), set())

    def test_one_empty_list(self):
        self.assertEqual(tuple_intersection([], [(1, 2)]), set())

    def test_no_intersection(self):
        self.assertEqual(tuple_intersection([(1, 2), (3, 4)], [(5, 6), (7, 8)]), set())

    def test_duplicate_tuples(self):
        self.assertEqual(tuple_intersection([(1, 2), (1, 2)], [(2, 1), (2, 1)]), {(1, 2)})

    def test_same_lists(self):
        self.assertEqual(tuple_intersection([(1, 2), (3, 4)], [(1, 2), (3, 4)]), {(1, 2), (3, 4)})

    def test_complex_intersection(self):
        self.assertEqual(tuple_intersection([(1, 2, 3), (4, 5, 6)], [(3, 2, 1), (6, 5, 4)]), {(1, 2, 3), (4, 5, 6)})
