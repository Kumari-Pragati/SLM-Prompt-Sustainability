import unittest
from mbpp_249_code import intersection_array

class TestIntersectionArray(unittest.TestCase):

    def test_intersection_array(self):
        self.assertEqual(intersection_array([1, 2, 3, 4, 5], [4, 5, 6, 7, 8]), [4, 5])
        self.assertEqual(intersection_array([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]), [])
        self.assertEqual(intersection_array([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(intersection_array([1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 2, 3, 4, 5])
        self.assertEqual(intersection_array([], []), [])
        self.assertEqual(intersection_array([1, 2, 3, 4, 5], []), [])
        self.assertEqual(intersection_array([], [1, 2, 3, 4, 5]), [])

    def test_intersection_array_empty_list(self):
        self.assertEqual(intersection_array([], []), [])
