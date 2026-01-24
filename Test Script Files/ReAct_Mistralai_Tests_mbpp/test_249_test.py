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

    def test_non_matching_elements(self):
        self.assertListEqual(intersection_array([1, 2, 3], [4, 5, 6]), [])

    def test_duplicate_elements(self):
        self.assertListEqual(intersection_array([1, 1, 2, 2], [2, 3]), [2])

    def test_negative_numbers(self):
        self.assertListEqual(intersection_array([-1, -2, -3], [-2, -3, 1]), [-2, -3])

    def test_mixed_types(self):
        self.assertRaises(TypeError, intersection_array, [1, 2, 3], [4, "x", 5])
