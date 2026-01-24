import unittest
from mbpp_101_code import kth_element

class TestKthElement(unittest.TestCase):
    def test_kth_element_valid_input(self):
        self.assertEqual(kth_element([1, 2, 3, 4, 5], 5, 3), 3)

    def test_kth_element_invalid_input(self):
        with self.assertRaises(IndexError):
            kth_element([1, 2, 3, 4, 5], 5, 6)

    def test_kth_element_empty_array(self):
        with self.assertRaises(IndexError):
            kth_element([], 0, 1)

    def test_kth_element_single_element_array(self):
        self.assertEqual(kth_element([1], 1, 1), 1)

    def test_kth_element_sorted_array(self):
        self.assertEqual(kth_element([1, 2, 3, 4, 5], 5, 5), 5)

    def test_kth_element_unsorted_array(self):
        self.assertEqual(kth_element([5, 2, 8, 3, 1], 5, 2), 2)
