import unittest
from mbpp_473_code import tuple_intersection

class TestTupleIntersection(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(tuple_intersection([(1, 2), (3, 4)], [(2, 1), (4, 3)]), ({(1, 2), (3, 4)},))

    def test_empty_lists(self):
        self.assertEqual(tuple_intersection([], []), set())

    def test_single_element_lists(self):
        self.assertEqual(tuple_intersection([(1,)], [(1,)]), ({(1,)},))

    def test_disjoint_lists(self):
        self.assertEqual(tuple_intersection([(1, 2), (3, 4)], [(5, 6)]), set())

    def test_common_elements(self):
        self.assertEqual(tuple_intersection([(1, 2), (2, 3)], [(2, 3), (4, 5)]), ({(2, 3)},))

    def test_duplicates(self):
        self.assertEqual(tuple_intersection([(1, 2), (2, 2), (3, 4)], [(2, 2), (4, 5)]), ({(2, 2), (2, 3)},))
