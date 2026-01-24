import unittest
from mbpp_249_code import intersection_array

class TestIntersectionArray(unittest.TestCase):

    def test_intersection_array_empty(self):
        self.assertEqual(intersection_array([], [1, 2, 3]), [])

    def test_intersection_array_single_element(self):
        self.assertEqual(intersection_array([1], [1, 2, 3]), [1])

    def test_intersection_array_multiple_elements(self):
        self.assertEqual(intersection_array([1, 2], [1, 2, 3]), [1, 2])

    def test_intersection_array_no_intersection(self):
        self.assertEqual(intersection_array([1, 2, 3], [4, 5, 6]), [])

    def test_intersection_array_duplicates(self):
        self.assertEqual(intersection_array([1, 1, 2], [1, 2, 2, 3]), [1, 2])

    def test_intersection_array_empty_second(self):
        self.assertEqual(intersection_array([1, 2, 3], []), [])
