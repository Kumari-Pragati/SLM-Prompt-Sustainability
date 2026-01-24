import unittest
from mbpp_101_code import kth_element

class TestKthElement(unittest.TestCase):

    def test_kth_element_positive(self):
        self.assertEqual(kth_element([1, 2, 3, 4, 5], 5, 1), 1)
        self.assertEqual(kth_element([1, 2, 3, 4, 5], 5, 5), 5)
        self.assertEqual(kth_element([1, 2, 3, 4, 5], 3, 3), 3)

    def test_kth_element_empty_list(self):
        self.assertRaises(IndexError, lambda: kth_element([], 1, 1))

    def test_kth_element_single_element(self):
        self.assertEqual(kth_element([1], 1, 1), 1)

    def test_kth_element_negative(self):
        self.assertRaises(IndexError, lambda: kth_element([1, 2, 3], 1, -1))
        self.assertRaises(IndexError, lambda: kth_element([1, 2, 3], 1, 0))
        self.assertRaises(IndexError, lambda: kth_element([1, 2, 3], 1, 4))

    def test_kth_element_out_of_order(self):
        self.assertEqual(kth_element([5, 3, 1, 4, 2], 5, 3), 3)
        self.assertEqual(kth_element([5, 3, 1, 4, 2], 5, 5), 5)

    def test_kth_element_duplicates(self):
        self.assertEqual(kth_element([1, 1, 2, 2, 3], 5, 1), 1)
        self.assertEqual(kth_element([1, 1, 2, 2, 3], 5, 2), 2)
        self.assertEqual(kth_element([1, 1, 2, 2, 3], 5, 3), 3)
