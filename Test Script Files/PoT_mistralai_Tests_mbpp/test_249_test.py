import unittest
from mbpp_249_code import intersection_array

class TestIntersectionArray(unittest.TestCase):

    def test_typical_case(self):
        self.assertListEqual(intersection_array([1, 2, 3, 4, 5], [5, 6, 7, 4, 5]), [4, 5])
        self.assertListEqual(intersection_array([1, 2, 3], [3, 4, 5]), [3])
        self.assertListEqual(intersection_array([1, 2, 3], []), [])
        self.assertListEqual(intersection_array([], [1, 2, 3]), [])
        self.assertListEqual(intersection_array([1, 1, 2, 2], [2, 3]), [2])

    def test_edge_case(self):
        self.assertListEqual(intersection_array([], [1]), [])
        self.assertListEqual(intersection_array([1], []), [])
        self.assertListEqual(intersection_array([1], [1]), [1])
        self.assertListEqual(intersection_array([1, 1], [1]), [1])
        self.assertListEqual(intersection_array([1, 1], [2]), [])

    def test_boundary_case(self):
        self.assertListEqual(intersection_array([-1, 0, 1], [-1, 0, 1]), [-1, 0, 1])
        self.assertListEqual(intersection_array([-1, 0, 1], [-1, 0, -1]), [-1])
        self.assertListEqual(intersection_array([-1, 0, 1], [-10, -1, 0, 1]), [-1])
        self.assertListEqual(intersection_array([-1, 0, 1], [1, 10]), [])
