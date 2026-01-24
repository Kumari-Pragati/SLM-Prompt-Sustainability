import unittest
from mbpp_799_code import left_Rotate

class TestLeftRotate(unittest.TestCase):

    def test_left_rotate_positive(self):
        self.assertEqual(left_Rotate(16, 2), 64)
        self.assertEqual(left_Rotate(8, 3), 64)
        self.assertEqual(left_Rotate(1, 31), 2**31)

    def test_left_rotate_zero(self):
        self.assertEqual(left_Rotate(0, 5), 0)

    def test_left_rotate_negative(self):
        self.assertEqual(left_Rotate(-16, 2), -64)
        self.assertEqual(left_Rotate(-8, 3), -64)
        self.assertEqual(left_Rotate(-1, 31), -2**31)

    def test_left_rotate_boundary(self):
        self.assertEqual(left_Rotate(2**31 - 1, 1), -2**31)
        self.assertEqual(left_Rotate(-2**31, 1), 2**31 - 1)
