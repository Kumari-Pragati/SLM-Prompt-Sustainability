import unittest
from mbpp_60_code import max_len_sub

class TestMaxLenSub(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5], 5), 5)

    def test_edge_cases(self):
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5], 1), 1)
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5], 5), 5)
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5], 0), 0)

    def test_special_cases(self):
        self.assertEqual(max_len_sub([1, 1, 1, 1, 1], 5), 1)
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5], 5), 5)
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5, 6], 6), 6)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            max_len_sub("abc", 5)
        with self.assertRaises(TypeError):
            max_len_sub([1, 2, 3], "five")
