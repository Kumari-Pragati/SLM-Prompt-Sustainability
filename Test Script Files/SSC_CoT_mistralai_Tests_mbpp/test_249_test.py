import unittest
from mbpp_249_code import list_ as mock_list

from _249_code import intersection_array

class TestIntersectionArray(unittest.TestCase):

    def test_intersection_normal(self):
        array_nums1 = [1, 2, 3, 4]
        array_nums2 = [3, 4, 5, 6]
        expected_result = [3, 4]
        self.assertEqual(intersection_array(array_nums1, array_nums2), expected_result)

    def test_intersection_edge_cases(self):
        array_nums1 = [1, 2, 3]
        array_nums2 = [3, 2, 1]
        expected_result = [1, 2, 3]
        self.assertEqual(intersection_array(array_nums1, array_nums2), expected_result)

        array_nums1 = [1, 2, 3]
        array_nums2 = [3, 2]
        expected_result = [2, 3]
        self.assertEqual(intersection_array(array_nums1, array_nums2), expected_result)

        array_nums1 = [1, 2]
        array_nums2 = [3, 2, 1]
        expected_result = [2]
        self.assertEqual(intersection_array(array_nums1, array_nums2), expected_result)

    def test_intersection_empty_arrays(self):
        array_nums1 = []
        array_nums2 = []
        expected_result = []
        self.assertEqual(intersection_array(array_nums1, array_nums2), expected_result)

        array_nums1 = [1, 2, 3]
        array_nums2 = []
        expected_result = []
        self.assertEqual(intersection_array(array_nums1, array_nums2), expected_result)

        array_nums1 = []
        array_nums2 = [1, 2, 3]
        expected_result = []
        self.assertEqual(intersection_array(array_nums1, array_nums2), expected_result)

    def test_intersection_single_element(self):
        array_nums1 = [1]
        array_nums2 = [1]
        expected_result = [1]
        self.assertEqual(intersection_array(array_nums1, array_nums2), expected_result)

        array_nums1 = [1]
        array_nums2 = [2]
        expected_result = []
        self.assertEqual(intersection_array(array_nums1, array_nums2), expected_result)

    def test_intersection_invalid_input(self):
        array_nums1 = 1
        array_nums2 = [2, 3]
        with self.assertRaises(TypeError):
            intersection_array(array_nums1, array_nums2)

        array_nums1 = [1, 2, 3]
        array_nums2 = 2
        with self.assertRaises(TypeError):
            intersection_array(array_nums1, array_nums2)
