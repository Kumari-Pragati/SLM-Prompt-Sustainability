import unittest
from mbpp_101_code import kth_element

class TestKthElement(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(kth_element([1, 2, 3, 4, 5], 5, 3), 3)

    def test_edge_case(self):
        self.assertEqual(kth_element([5, 4, 3, 2, 1], 5, 1), 1)
        self.assertEqual(kth_element([1, 2, 3, 4, 5], 5, 5), 5)

    def test_invalid_input(self):
        with self.assertRaises(IndexError):
            kth_element([1, 2, 3], 2, 4)

    def test_k_out_of_range(self):
        with self.assertRaises(IndexError):
            kth_element([1, 2, 3], 3, 7)

    def test_empty_array(self):
        with self.assertRaises(IndexError):
            kth_element([], 0, 1)

    def test_single_element_array(self):
        self.assertEqual(kth_element([1], 1, 1), 1)

    def test_array_with_duplicates(self):
        self.assertEqual(kth_element([1, 2, 2, 3, 4, 5], 6, 3), 3)
