import unittest
from mbpp_536_code import nth_items

class TestNthItems(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(nth_items([1, 2, 3, 4, 5, 6, 7, 8, 9], 2), [1, 3, 5, 7, 9])

    def test_typical_case_with_negative_numbers(self):
        self.assertEqual(nth_items([-1, -2, -3, -4, -5, -6, -7, -8, -9], 2), [-1, -3, -5, -7, -9])

    def test_typical_case_with_zero(self):
        self.assertEqual(nth_items([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 2), [0, 2, 4, 6, 8])

    def test_edge_case_with_single_element(self):
        self.assertEqual(nth_items([1], 1), [1])
        self.assertEqual(nth_items([1], 2), [])

    def test_edge_case_with_empty_list(self):
        self.assertEqual(nth_items([], 1), [])
        self.assertEqual(nth_items([], 2), [])

    def test_invalid_input_negative_step(self):
        with self.assertRaises(IndexError):
            nth_items([1, 2, 3, 4, 5], -1)

    def test_invalid_input_zero_step(self):
        with self.assertRaises(IndexError):
            nth_items([1, 2, 3, 4, 5], 0)
