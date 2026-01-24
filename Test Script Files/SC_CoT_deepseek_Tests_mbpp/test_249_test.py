import unittest
from mbpp_249_code import intersection_array

class TestIntersectionArray(unittest.TestCase):

    def test_typical_case(self):
        array_nums1 = [1, 2, 2, 1]
        array_nums2 = [2, 2]
        self.assertEqual(intersection_array(array_nums1, array_nums2), [2, 2])

    def test_empty_array(self):
        array_nums1 = []
        array_nums2 = [1, 2, 3]
        self.assertEqual(intersection_array(array_nums1, array_nums2), [])

    def test_edge_case(self):
        array_nums1 = [1, 2, 3, 4, 5]
        array_nums2 = [5, 6, 7, 8, 9]
        self.assertEqual(intersection_array(array_nums1, array_nums2), [5])

    def test_corner_case(self):
        array_nums1 = [10, 20, 30, 40, 50]
        array_nums2 = [10, 20, 30, 40, 50]
        self.assertEqual(intersection_array(array_nums1, array_nums2), [10, 20, 30, 40, 50])

    def test_invalid_input(self):
        array_nums1 = "1,2,3,4,5"
        array_nums2 = [1, 2, 3, 4, 5]
        with self.assertRaises(TypeError):
            intersection_array(array_nums1, array_nums2)
