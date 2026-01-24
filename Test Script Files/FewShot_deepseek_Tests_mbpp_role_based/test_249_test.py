import unittest
from mbpp_249_code import intersection_array

class TestIntersectionArray(unittest.TestCase):
    def test_typical_use_case(self):
        array_nums1 = [1, 2, 3, 4, 5]
        array_nums2 = [4, 5, 6, 7, 8]
        self.assertEqual(intersection_array(array_nums1, array_nums2), [4, 5])

    def test_edge_case_empty_arrays(self):
        array_nums1 = []
        array_nums2 = []
        self.assertEqual(intersection_array(array_nums1, array_nums2), [])

    def test_boundary_case_one_empty_array(self):
        array_nums1 = []
        array_nums2 = [1, 2, 3]
        self.assertEqual(intersection_array(array_nums1, array_nums2), [])

    def test_boundary_case_identical_arrays(self):
        array_nums1 = [1, 2, 3]
        self.assertEqual(intersection_array(array_nums1, array_nums1), array_nums1)

    def test_invalid_input_non_list_input(self):
        array_nums1 = "1,2,3"
        array_nums2 = [1, 2, 3]
        with self.assertRaises(TypeError):
            intersection_array(array_nums1, array_nums2)
