import unittest
from mbpp_536_code import nth_items

class TestNthItems(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(nth_items([1, 2, 3, 4, 5], 2), [2, 4])
        self.assertEqual(nth_items([1, 2, 3, 4, 5], 3), [3, 6])
        self.assertEqual(nth_items([1, 2, 3, 4, 5], 4), [4, 5])
        self.assertEqual(nth_items([1, 2, 3, 4, 5], 5), [5])

    def test_edge_cases(self):
        self.assertEqual(nth_items([1, 2, 3, 4, 5], 1), [1, 2, 3, 4, 5])
        self.assertEqual(nth_items([1, 2, 3, 4, 5], 0), [])
        self.assertEqual(nth_items([], 2), [])
        self.assertEqual(nth_items([1], 2), [])

    def test_negative_n(self):
        with self.assertRaises(ValueError):
            nth_items([1, 2, 3, 4, 5], -1)

    def test_non_integer_n(self):
        with self.assertRaises(TypeError):
            nth_items([1, 2, 3, 4, 5], 3.14)
