import unittest
from mbpp_799_code import left_Rotate

class TestLeftRotate(unittest.TestCase):

    def test_left_rotate_positive(self):
        self.assertEqual(left_Rotate(12, 2), 48)
        self.assertEqual(left_Rotate(25, 1), 256)
        self.assertEqual(left_Rotate(100, 3), 6400)

    def test_left_rotate_zero(self):
        self.assertEqual(left_Rotate(0, 2), 0)

    def test_left_rotate_negative(self):
        self.assertEqual(left_Rotate(-12, 2), -16)
        self.assertEqual(left_Rotate(-25, 1), -256)
        self.assertEqual(left_Rotate(-100, 3), -6400)

    def test_left_rotate_large_number(self):
        self.assertEqual(left_Rotate(2147483647, 1), 2147483648)

    def test_left_rotate_out_of_range(self):
        self.assertRaises(ValueError, left_Rotate, 2147483647, 33)
        self.assertRaises(ValueError, left_Rotate, -2147483648, 33)
