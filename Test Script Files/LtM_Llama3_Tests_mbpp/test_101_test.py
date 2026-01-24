import unittest
from mbpp_101_code import kth_element

class TestKthElement(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(kth_element([1, 2, 3, 4, 5], 5, 3), 3)
        self.assertEqual(kth_element([5, 4, 3, 2, 1], 5, 1), 1)
        self.assertEqual(kth_element([1, 2, 3, 4, 5], 5, 5), 5)

    def test_edge(self):
        self.assertEqual(kth_element([1], 1, 1), 1)
        self.assertEqual(kth_element([1, 2], 2, 1), 1)
        self.assertEqual(kth_element([1, 2, 3], 3, 1), 1)
        self.assertEqual(kth_element([1, 2, 3], 3, 3), 3)

    def test_invalid(self):
        with self.assertRaises(IndexError):
            kth_element([], 0, 1)
        with self.assertRaises(IndexError):
            kth_element([1, 2, 3], 3, 6)
        with self.assertRaises(TypeError):
            kth_element('abc', 3, 1)
