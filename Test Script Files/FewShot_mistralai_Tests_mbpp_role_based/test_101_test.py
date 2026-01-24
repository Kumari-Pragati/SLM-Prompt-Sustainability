import unittest
from mbpp_101_code import kth_element

class TestKthElement(unittest.TestCase):
    def test_kth_element_positive(self):
        self.assertEqual(kth_element([1, 2, 3, 4, 5], 3, 3), 4)
        self.assertEqual(kth_element([6, 5, 4, 3, 2, 1], 6, 1), 1)
        self.assertEqual(kth_element([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 11, 1), 1)

    def test_kth_element_negative(self):
        self.assertRaises(IndexError, lambda: kth_element([1, 2, 3], 0, 1))
        self.assertRaises(IndexError, lambda: kth_element([1, 2, 3], 4, 1))
        self.assertRaises(ValueError, lambda: kth_element([1, 2, 3], 3, 0))
        self.assertRaises(ValueError, lambda: kth_element([1, 2, 3], 3, 4))
        self.assertRaises(TypeError, lambda: kth_element('1, 2, 3', 3, 1))
