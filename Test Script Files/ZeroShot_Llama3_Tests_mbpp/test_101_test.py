import unittest
from mbpp_101_code import kth_element

class TestKthElement(unittest.TestCase):

    def test_kth_element(self):
        self.assertEqual(kth_element([5, 3, 8, 6, 7, 2], 6, 3), 6)
        self.assertEqual(kth_element([5, 3, 8, 6, 7, 2], 6, 1), 5)
        self.assertEqual(kth_element([5, 3, 8, 6, 7, 2], 6, 6), 2)
        self.assertEqual(kth_element([5, 3, 8, 6, 7, 2], 6, 7), 7)
        self.assertEqual(kth_element([5, 3, 8, 6, 7, 2], 6, 4), 7)
        self.assertEqual(kth_element([5, 3, 8, 6, 7, 2], 6, 5), 6)
        self.assertEqual(kth_element([5, 3, 8, 6, 7, 2], 6, 2), 8)
        self.assertEqual(kth_element([5, 3, 8, 6, 7, 2], 6, 6), 2)
        self.assertEqual(kth_element([5, 3, 8, 6, 7, 2], 6, 0), 5)
        self.assertEqual(kth_element([5, 3, 8, 6, 7, 2], 6, 6), 2)

    def test_kth_element_invalid_input(self):
        with self.assertRaises(IndexError):
            kth_element([5, 3, 8, 6, 7, 2], 5, 6)
        with self.assertRaises(IndexError):
            kth_element([5, 3, 8, 6, 7, 2], 6, 7)
