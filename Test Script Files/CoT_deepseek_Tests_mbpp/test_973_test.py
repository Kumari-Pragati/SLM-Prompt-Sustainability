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
        self.assertEqual(left_rotate('abcdefg', 8), 'abcdefg')

    def test_invalid_input_string(self):
        with self.assertRaises(TypeError):
            left_rotate(123456, 2)

    def test_invalid_input_rotation(self):
        with self.assertRaises(TypeError):
            left_rotate('abcdefg', 'two')
