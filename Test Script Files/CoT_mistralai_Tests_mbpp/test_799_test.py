import unittest
from mbpp_799_code import left_Rotate

class TestLeftRotate(unittest.TestCase):
    def test_left_rotate_positive(self):
        self.assertEqual(left_Rotate(12, 2), 48)
        self.assertEqual(left_Rotate(256, 1), 512)
        self.assertEqual(left_Rotate(1000, 3), 32)

    def test_left_rotate_zero(self):
        self.assertEqual(left_Rotate(0, 2), 0)

    def test_left_rotate_negative(self):
        self.assertEqual(left_Rotate(-12, 2), 194)
        self.assertEqual(left_Rotate(-256, 1), -254)
        self.assertEqual(left_Rotate(-1000, 3), -996)

    def test_left_rotate_boundary(self):
        self.assertEqual(left_Rotate(1, 0), 0)
        self.assertEqual(left_Rotate(1, 31), 2147483648)
        self.assertEqual(left_Rotate(1, 32), 0)

    def test_left_rotate_invalid(self):
        self.assertRaises(ValueError, left_Rotate, 12, 33)
        self.assertRaises(ValueError, left_Rotate, -12, -1)
