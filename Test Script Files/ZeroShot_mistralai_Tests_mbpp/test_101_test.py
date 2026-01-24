import unittest
from mbpp_101_code import kth_element

class TestKthElement(unittest.TestCase):

    def test_kth_element_empty_list(self):
        self.assertRaises(IndexError, kth_element, [], 1, 1)

    def test_kth_element_single_element(self):
        self.assertEqual(kth_element([1], 1, 1), 1)

    def test_kth_element_small_list(self):
        self.assertEqual(kth_element([1, 2, 3], 3, 2), 2)

    def test_kth_element_large_list(self):
        self.assertEqual(kth_element([1, 5, 2, 6, 3, 7, 4], 7, 4), 4)

    def test_kth_element_large_list_k_1(self):
        self.assertEqual(kth_element([1, 5, 2, 6, 3, 7, 4], 7, 1), 1)

    def test_kth_element_large_list_k_8(self):
        self.assertEqual(kth_element([1, 5, 2, 6, 3, 7, 4], 7, 8), 5)
