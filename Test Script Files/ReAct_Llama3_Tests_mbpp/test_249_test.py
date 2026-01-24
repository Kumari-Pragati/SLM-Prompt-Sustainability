import unittest
from mbpp_249_code import intersection_array

class TestIntersectionArray(unittest.TestCase):

    def test_intersection_array_typical(self):
        self.assertEqual(intersection_array([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]), [3, 4, 5])

    def test_intersection_array_empty(self):
        self.assertEqual(intersection_array([1, 2, 3, 4, 5], []), [])

    def test_intersection_array_single_element(self):
        self.assertEqual(intersection_array([1], [1, 2, 3, 4, 5]), [1])

    def test_intersection_array_no_intersection(self):
        self.assertEqual(intersection_array([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]), [])

    def test_intersection_array_duplicates(self):
        self.assertEqual(intersection_array([1, 2, 2, 3, 4], [2, 2, 3, 4, 5]), [2, 2, 3, 4])

    def test_intersection_array_duplicates_order(self):
        self.assertEqual(intersection_array([1, 2, 2, 3, 4], [4, 3, 2, 2, 1]), [1, 2, 2, 3, 4])
