import unittest
from mbpp_60_code import max_len_sub

class TestMaxLenSub(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(max_len_sub([], 0), 0)

    def test_single_element_array(self):
        for n in [1]:
            for arr in [[1], [-1], [0]]:
                self.assertEqual(max_len_sub(arr, n[0]), 1)

    def test_two_elements_array(self):
        for arr in [[1, 2], [-1, -2], [0, 1], [1, 0], [-1, 1], [1, -1], [0, 0]]:
            self.assertEqual(max_len_sub(arr, len(arr)), 2)

    def test_three_elements_array(self):
        for arr in [[1, 2, 3], [-1, -2, -3], [0, 1, 2], [1, 0, 1], [-1, 1, -1], [1, -1, 1], [0, 0, 1], [1, 0, -1], [-1, 0, 1]]:
            self.assertEqual(max_len_sub(arr, len(arr)), 3)

    def test_four_elements_array(self):
        for arr in [[1, 2, 3, 4], [-1, -2, -3, -4], [0, 1, 2, 3], [1, 0, 1, 2], [-1, 1, -1, 1], [1, -1, 1, -1], [0, 0, 1, 2], [1, 0, -1, 0], [-1, 0, 1, 0], [0, 1, 0, 1]]:
            self.assertEqual(max_len_sub(arr, len(arr)), 4)

    def test_negative_n(self):
        for arr in [[1, 2, 3], [-1, -2, -3], [0, 1, 2], [1, 0, 1], [-1, 1, -1], [1, -1, 1], [0, 0, 1], [1, 0, -1], [-1, 0, 1], [0, 1, 0]]:
            with self.assertRaises(ValueError):
                max_len_sub(arr, -1)

    def test_n_larger_than_array_length(self):
        for arr in [[1, 2, 3], [-1, -2, -3], [0, 1, 2], [1, 0, 1], [-1, 1, -1], [1, -1, 1], [0, 0, 1], [1, 0, -1], [-1, 0, 1], [0, 1, 0]]:
            with self.assertRaises(ValueError):
                max_len_sub(arr, len(arr) + 1)
