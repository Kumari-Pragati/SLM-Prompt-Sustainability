import unittest
from mbpp_328_code import rotate_left

class TestRotateLeft(unittest.TestCase):

    def test_rotate_left_valid_input(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 2, 4), [3, 4, 5, 1, 2])

    def test_rotate_left_invalid_input_type(self):
        with self.assertRaises(TypeError):
            rotate_left("hello", 2, 4)

    def test_rotate_left_invalid_input_value(self):
        with self.assertRaises(IndexError):
            rotate_left([1, 2, 3, 4, 5], 5, 4)

    def test_rotate_left_invalid_input_range(self):
        with self.assertRaises(IndexError):
            rotate_left([1, 2, 3, 4, 5], 6, 4)
