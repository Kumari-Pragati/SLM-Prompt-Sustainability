import unittest
from mbpp_60_code import max_len_sub

class TestMaxLenSub(unittest.TestCase):

    def test_max_len_sub(self):
        self.assertEqual(max_len_sub([10, 22, 9, 33, 21, 50, 41, 60, 80], 9), 5)
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 9)
        self.assertEqual(max_len_sub([90, 70, 20, 80, 50], 5), 2)
        self.assertEqual(max_len_sub([10, 15, 20, 25, 30], 5), 5)
        self.assertEqual(max_len_sub([10, 10, 10, 10, 10], 5), 5)
