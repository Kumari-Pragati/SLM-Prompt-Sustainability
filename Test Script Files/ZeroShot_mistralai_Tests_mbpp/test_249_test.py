import unittest
from mbpp_249_code import intersection_array

class TestIntersectionArray(unittest.TestCase):

    def test_empty_arrays(self):
        self.assertListEqual(intersection_array([], []), [])

    def test_single_element_arrays(self):
        self.assertListEqual(intersection_array([1], []), [])
        self.assertListEqual(intersection_array([], [1]), [])
        self.assertListEqual(intersection_array([1], [1]), [1])

    def test_identical_arrays(self):
        self.assertListEqual(intersection_array([1, 2, 3], [3, 2, 1]), [1, 2, 3])

    def test_overlapping_arrays(self):
        self.assertListEqual(intersection_array([1, 2, 3], [3, 4, 5]), [3])
        self.assertListEqual(intersection_array([4, 5, 6], [1, 2, 3]), [])
        self.assertListEqual(intersection_array([2, 3, 4], [1, 2, 3, 4, 5]), [2, 3, 4])

    def test_non_overlapping_arrays(self):
        self.assertListEqual(intersection_array([1, 2, 3], [4, 5, 6]), [])
        self.assertListEqual(intersection_array([4, 5, 6], [1, 2, 3]), [])
