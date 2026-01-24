import unittest
from mbpp_973_code import left_rotate

class TestLeftRotate(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(left_rotate('abcdefg', 2), 'cdefgab')

    def test_edge_case_d_equal_to_zero(self):
        self.assertEqual(left_rotate('abcdefg', 0), 'abcdefg')

    def test_edge_case_d_equal_to_length(self):
        self.assertEqual(left_rotate('abcdefg', 7), 'abcdefg')

    def test_edge_case_d_greater_than_length(self):
        self.assertEqual(left_rotate('abcdefg', 8), 'abcdefg')

    def test_corner_case_empty_string(self):
        self.assertEqual(left_rotate('', 2), '')

    def test_invalid_input_d_negative(self):
        with self.assertRaises(IndexError):
            left_rotate('abcdefg', -1)

    def test_invalid_input_s_not_string(self):
        with self.assertRaises(TypeError):
            left_rotate(123456, 2)
