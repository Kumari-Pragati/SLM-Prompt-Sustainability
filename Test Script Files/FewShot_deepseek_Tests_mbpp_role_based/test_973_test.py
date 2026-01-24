import unittest
from mbpp_973_code import left_rotate

class TestLeftRotate(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(left_rotate('abcdefg', 2), 'cdefgab')

    def test_boundary_conditions(self):
        self.assertEqual(left_rotate('abc', 0), 'abc')
        self.assertEqual(left_rotate('abc', 3), 'abc')
        self.assertEqual(left_rotate('abc', 4), 'abc')

    def test_edge_cases(self):
        self.assertEqual(left_rotate('', 2), '')
        self.assertEqual(left_rotate('a', 1), 'a')
        self.assertEqual(left_rotate('abc', 1), 'bca')

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            left_rotate('abc', '2')
        with self.assertRaises(TypeError):
            left_rotate(123, 2)
