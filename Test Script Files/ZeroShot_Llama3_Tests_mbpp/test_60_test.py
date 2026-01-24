import unittest
from mbpp_60_code import max_len_sub

class TestMaxLenSub(unittest.TestCase):

    def test_max_len_sub(self):
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5], 5), 5)
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5, 6], 6), 6)
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5, 6, 7], 7), 7)
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5, 6, 7, 8], 8), 7)
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 7)
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 7)
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 11), 7)
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 12), 7)
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 13), 7)
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], 14), 7)
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 15), 7)
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 16), 7)
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 17), 7)
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], 18), 7)
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 19), 7)
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 20), 7)
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21], 21), 7)
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22], 22), 7)
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,