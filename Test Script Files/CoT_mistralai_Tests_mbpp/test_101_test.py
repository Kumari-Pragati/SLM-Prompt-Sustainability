import unittest
from mbpp_101_code import kth_element

class TestKthElement(unittest.TestCase):
    def test_kth_element_valid_inputs(self):
        self.assertEqual(kth_element([1, 2, 3, 4, 5], 5, 3), 4)
        self.assertEqual(kth_element([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 10, 5), 6)
        self.assertEqual(kth_element([3, 2, 1], 3, 1), 1)
        self.assertEqual(kth_element([1, 1, 1, 1, 1], 5, 1), 1)
        self.assertEqual(kth_element([-5, -4, -3, -2, -1], 5, 2), -4)

    def test_kth_element_invalid_inputs(self):
        self.assertRaises(IndexError, lambda: kth_element([1, 2, 3], 0, 1))
        self.assertRaises(IndexError, lambda: kth_element([1, 2, 3], 4, 0))
        self.assertRaises(IndexError, lambda: kth_element([1, 2, 3], 4, 5))
        self.assertRaises(ValueError, lambda: kth_element([1, 2, 3], 4, 0))
        self.assertRaises(ValueError, lambda: kth_element([1, 2, 3], 4, -1))
        self.assertRaises(ValueError, lambda: kth_element([1, 2, 3], -1, 1))
        self.assertRaises(ValueError, lambda: kth_element([], 4, 1))
        self.assertRaises(ValueError, lambda: kth_element([1], 0, 1))
