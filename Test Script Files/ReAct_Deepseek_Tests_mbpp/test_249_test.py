import unittest
from mbpp_249_code import intersection_array

class TestIntersectionArray(unittest.TestCase):

    def test_typical_case(self):
        array_nums1 = [1, 2, 3, 4, 5]
        array_nums2 = [4, 5, 6, 7, 8]
        result = intersection_array(array_nums1, array_nums2)
        self.assertEqual(result, [4, 5])

    def test_empty_arrays(self):
        array_nums1 = []
        array_nums2 = []
        result = intersection_array(array_nums1, array_nums2)
        self.assertEqual(result, [])

    def test_one_empty_array(self):
        array_nums1 = [1, 2, 3]
        array_nums2 = []
        result = intersection_array(array_nums1, array_nums2)
        self.assertEqual(result, [])

    def test_duplicate_elements(self):
        array_nums1 = [1, 2, 2, 3]
        array_nums2 = [2, 2, 3, 4]
        result = intersection_array(array_nums1, array_nums2)
        self.assertEqual(result, [2, 2, 3])

    def test_same_arrays(self):
        array_nums1 = [1, 2, 3, 4, 5]
        array_nums2 = [1, 2, 3, 4, 5]
        result = intersection_array(array_nums1, array_nums2)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_no_intersection(self):
        array_nums1 = [1, 2, 3, 4, 5]
        array_nums2 = [6, 7, 8, 9, 10]
        result = intersection_array(array_nums1, array_nums2)
        self.assertEqual(result, [])
