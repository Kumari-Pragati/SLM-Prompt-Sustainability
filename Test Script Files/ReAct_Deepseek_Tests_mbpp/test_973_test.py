import unittest
from mbpp_973_code import left_rotate

class TestLeftRotate(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(left_rotate('abcdefg', 2), 'cdefgab')

    def test_edge_case_zero_rotation(self):
        self.assertEqual(left_rotate('abcdefg', 0), 'abcdefg')

    def test_edge_case_full_rotation(self):
        self.assertEqual(left_rotate('abcdefg', 7), 'abcdefg')

    def test_edge_case_greater_rotation(self):
        self.assertEqual(left_rotate('abcdefg', 8), 'gabcdef')

    def test_edge_case_large_string(self):
        long_string = 'abcdefghijklmnopqrstuvwxyz'
        self.assertEqual(left_rotate(long_string, 5), 'fghijklmnopqrstuvwxyzabcde')

    def test_error_case_empty_string(self):
        self.assertEqual(left_rotate('', 2), '')

    def test_error_case_negative_rotation(self):
        with self.assertRaises(IndexError):
            left_rotate('abcdefg', -1)
