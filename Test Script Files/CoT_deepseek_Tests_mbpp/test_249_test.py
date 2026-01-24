import unittest
from mbpp_249_code import intersection_array

class TestIntersectionArray(unittest.TestCase):

    def test_typical_case(self):
        array_nums1 = [1, 2, 3, 4, 5]
        array_nums2 = [4, 5, 6, 7, 8]
        expected_output = [4, 5]
        self.assertEqual(intersection_array(array_nums1, array_nums2), expected_output)

    def test_empty_array(self):
        array_nums1 = []
        array_nums2 = [4, 5, 6, 7, 8]
        expected_output = []
        self.assertEqual(intersection_array(array_nums1, array_nums2), expected_output)

    def test_duplicate_elements(self):
        array_nums1 = [1, 2, 2, 3, 4]
        array_nums2 = [2, 2, 4, 4, 5]
        expected_output = [2, 2, 4]
        self.assertEqual(intersection_array(array_nums1, array_nums2), expected_output)

    def test_no_intersection(self):
        array_nums1 = [1, 2, 3, 4, 5]
        array_nums2 = [6, 7, 8, 9, 10]
        expected_output = []
        self.assertEqual(intersection_array(array_nums1, array_nums2), expected_output)

    def test_same_arrays(self):
        array_nums1 = [1, 2, 3, 4, 5]
        array_nums2 = [1, 2, 3, 4, 5]
        expected_output = [1, 2, 3, 4, 5]
        self.assertEqual(intersection_array(array_nums1, array_nums2), expected_output)
