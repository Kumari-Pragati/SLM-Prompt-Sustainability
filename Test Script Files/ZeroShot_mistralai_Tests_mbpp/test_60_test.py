import unittest
from mbpp_60_code import max_len_sub

class TestMaxLenSub(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_len_sub([], 0), 0)

    def test_single_element(self):
        self.assertEqual(max_len_sub([1], 1), 1)

    def test_two_elements(self):
        self.assertEqual(max_len_sub([1, 2], 2), 2)

    def test_three_elements(self):
        self.assertEqual(max_len_sub([1, 2, 3], 3), 3)

    def test_four_elements(self):
        self.assertEqual(max_len_sub([1, 2, 3, 4], 4), 4)

    def test_five_elements(self):
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5], 5), 5)

    def test_decreasing_sequence(self):
        self.assertEqual(max_len_sub([5, 4, 3, 2, 1], 5), 5)

    def test_increasing_sequence(self):
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5], 5), 5)

    def test_alternating_sequence(self):
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5, 4, 3, 2, 1], 9), 5)

    def test_random_sequence(self):
        arr = [3, 8, 9, 1, 2, 5, 2, 3, 7, 8, 4, 8, 5, 9, 7, 2, 4, 6, 5, 3, 5]
        self.assertEqual(max_len_sub(arr, len(arr)), 4)
