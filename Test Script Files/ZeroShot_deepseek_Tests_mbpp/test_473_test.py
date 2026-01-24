import unittest
from mbpp_473_code import tuple_intersection

class TestTupleIntersection(unittest.TestCase):

    def test_empty_lists(self):
        self.assertEqual(tuple_intersection([], []), set())

    def test_single_element_lists(self):
        self.assertEqual(tuple_intersection([(1, 2, 3)], [(1, 2, 3)]), {(1, 2, 3)})
        self.assertEqual(tuple_intersection([(1, 2, 3)], []), set())
        self.assertEqual(tuple_intersection([], [(1, 2, 3)]), set())

    def test_multiple_element_lists(self):
        self.assertEqual(tuple_intersection([(1, 2, 3), (4, 5, 6)], [(1, 2, 3), (4, 5, 6)]), {(1, 2, 3), (4, 5, 6)})
        self.assertEqual(tuple_intersection([(1, 2, 3), (4, 5, 6)], [(4, 5, 6), (7, 8, 9)]), {(4, 5, 6)})
        self.assertEqual(tuple_intersection([(1, 2, 3), (4, 5, 6)], [(7, 8, 9)]), set())

    def test_duplicate_elements(self):
        self.assertEqual(tuple_intersection([(1, 2, 3), (1, 2, 3)], [(1, 2, 3), (1, 2, 3)]), {(1, 2, 3)})
        self.assertEqual(tuple_intersection([(1, 2, 3), (1, 2, 3)], [(1, 2, 3)]), {(1, 2, 3)})
        self.assertEqual(tuple_intersection([(1, 2, 3)], [(1, 2, 3), (1, 2, 3)]), {(1, 2, 3)})
