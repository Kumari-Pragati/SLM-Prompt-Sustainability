import unittest
from mbpp_101_code import kth_element

class TestKthElement(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(kth_element([1, 2, 3, 4, 5], 5, 3), 3)
        self.assertEqual(kth_element([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 11, 6), 5)
        self.assertEqual(kth_element([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5], 12, 7), 3)

    def test_edge_case_small_array(self):
        self.assertEqual(kth_element([1], 1, 1), 1)
        self.assertEqual(kth_element([1, 2], 2, 2), 2)
        self.assertEqual(kth_element([1, 2, 3], 3, 3), 3)

    def test_edge_case_k_larger_than_n(self):
        self.assertRaises(IndexError, lambda: kth_element([1, 2, 3], 3, 4))
        self.assertRaises(IndexError, lambda: kth_element([1, 2, 3], 2, 4))
        self.assertRaises(IndexError, lambda: kth_element([1, 2, 3], 1, 4))

    def test_edge_case_k_equal_to_n(self):
        self.assertEqual(kth_element([1, 2, 3], 3, 3), 3)

    def test_edge_case_k_less_than_1(self):
        self.assertRaises(ValueError, lambda: kth_element([1, 2, 3], 3, 0))
        self.assertRaises(ValueError, lambda: kth_element([1, 2, 3], 3, -1))
        self.assertRaises(ValueError, lambda: kth_element([1, 2, 3], 3, -2))

    def test_corner_case_duplicates(self):
        self.assertEqual(kth_element([1, 1, 2, 2, 3], 5, 3), 3)
        self.assertEqual(kth_element([1, 1, 1, 2, 2, 3], 6, 4), 2)
