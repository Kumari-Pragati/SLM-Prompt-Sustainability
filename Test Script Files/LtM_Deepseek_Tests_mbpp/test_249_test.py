import unittest
from mbpp_249_code import intersection_array

class TestIntersectionArray(unittest.TestCase):

    def test_simple_intersection(self):
        self.assertEqual(intersection_array([1,2,2,1], [2,2]), [2,2])

    def test_empty_arrays(self):
        self.assertEqual(intersection_array([], []), [])
        self.assertEqual(intersection_array([1,2,3], []), [])
        self.assertEqual(intersection_array([], [1,2,3]), [])

    def test_single_element_arrays(self):
        self.assertEqual(intersection_array([1], [1]), [1])
        self.assertEqual(intersection_array([1], [2]), [])

    def test_no_intersection(self):
        self.assertEqual(intersection_array([1,2,3], [4,5,6]), [])

    def test_duplicates_in_arrays(self):
        self.assertEqual(intersection_array([1,2,2], [2,2]), [2,2])

    def test_large_arrays(self):
        large_array = list(range(1, 10001))
        self.assertEqual(intersection_array(large_array, large_array), large_array)
