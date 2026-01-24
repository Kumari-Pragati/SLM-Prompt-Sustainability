import unittest
from mbpp_249_code import intersection_array

class TestIntersectionArray(unittest.TestCase):

    def test_simple_intersection(self):
        self.assertListEqual(intersection_array([1, 2, 3], [3, 4, 5]), [3])
        self.assertListEqual(intersection_array([4, 5, 6], [1, 2, 3]), [])
        self.assertListEqual(intersection_array([1, 1, 2, 2], [2, 3]), [2])

    def test_edge_cases(self):
        self.assertListEqual(intersection_array([], []), [])
        self.assertListEqual(intersection_array([1], []), [])
        self.assertListEqual(intersection_array([], [1]), [])
        self.assertListEqual(intersection_array([1], [1]), [1])
        self.assertListEqual(intersection_array([1, 2, 3], [3, 2, 1]), [1, 2, 3])
        self.assertListEqual(intersection_array([1, 2, 3], [3, 4, 3]), [3])

    def test_complex_scenarios(self):
        self.assertListEqual(intersection_array([1, 2, 3, 4], [4, 5, 6, 7, 4]), [4])
        self.assertListEqual(intersection_array([1, 2, 3, 4], [4, 5, 6, 7, 4, 1]), [4, 1])
        self.assertListEqual(intersection_array([1, 2, 3, 4], [4, 5, 6, 7, 4, 1, 2]), [4, 1, 2])
