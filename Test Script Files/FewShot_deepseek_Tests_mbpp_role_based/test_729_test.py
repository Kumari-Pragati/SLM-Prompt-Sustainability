import unittest
from mbpp_729_code import add_list

class TestAddList(unittest.TestCase):
    def test_typical_use_case(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        self.assertEqual(add_list(nums1, nums2), [5, 7, 9])

    def test_edge_condition(self):
        nums1 = [0]
        nums2 = [0]
        self.assertEqual(add_list(nums1, nums2), [0])

    def test_boundary_condition(self):
        nums1 = list(range(1, 1001))
        nums2 = list(range(1, 1001))
        self.assertEqual(add_list(nums1, nums2), list(range(2, 2002)))

    def test_invalid_input(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5]
        with self.assertRaises(ValueError):
            add_list(nums1, nums2)
