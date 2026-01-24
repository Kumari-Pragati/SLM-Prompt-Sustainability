import unittest
from mbpp_473_code import tuple_intersection

class TestTupleIntersection(unittest.TestCase):

    def test_normal_input(self):
        self.assertListEqual(tuple_intersection([(1, 2), (3, 4), (1, 3)], [(1, 2), (3, 4), (2, 3)]), [(1, 2)])
        self.assertListEqual(tuple_intersection([(1.0, 2.0), (3.0, 4.0), (1.0, 3.0)], [(1.0, 2.0), (3.0, 4.0), (2.0, 3.0)]), [(1.0, 2.0)])

    def test_edge_cases(self):
        self.assertListEqual(tuple_intersection([], []), [])
        self.assertListEqual(tuple_intersection([(1, 2)], []), [])
        self.assertListEqual(tuple_intersection([], [(1, 2)]), [])
        self.assertListEqual(tuple_intersection([(1, 2)], [(1, 2), (1, 3)]), [(1, 2)])
        self.assertListEqual(tuple_intersection([(1, 2)], [(2, 1)]), [])
        self.assertListEqual(tuple_intersection([(1, 2), (2, 1)], [(1, 2)]), [(1, 2)])

    def test_boundary_cases(self):
        self.assertListEqual(tuple_intersection([(0, 0), (1, 1)], [(0, 0), (1, 1), (1, 2)]), [(0, 0)])
        self.assertListEqual(tuple_intersection([(1, 2), (3, 4)], [(1, 2), (3, 4), (1, 3)]), [(1, 2)])
        self.assertListEqual(tuple_intersection([(1.0, 2.0), (3.0, 4.0)], [(1.0, 2.0), (3.0, 4.0), (1.0, 3.0)]), [(1.0, 2.0)])
