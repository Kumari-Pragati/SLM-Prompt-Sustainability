import unittest
from mbpp_60_code import max_len_sub

class TestMaxLenSub(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5], 5), 5)

    def test_edge(self):
        self.assertEqual(max_len_sub([1, 1, 1, 1, 1], 5), 1)
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5, 5], 6), 5)
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5, 6, 7], 7), 5)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            max_len_sub([], 0)
        with self.assertRaises(TypeError):
            max_len_sub([1, 2, 3], 'a')

    def test_complex(self):
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 5)
        self.assertEqual(max_len_sub([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 10), 5)
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 5)
