import unittest
from mbpp_799_code import left_Rotate

class TestLeftRotate(unittest.TestCase):
    def test_positive_shift(self):
        self.assertEqual(left_Rotate(123, 2), 492)
        self.assertEqual(left_Rotate(12345, 3), 12348)

    def test_zero_shift(self):
        self.assertEqual(left_Rotate(0, 0), 0)
        self.assertEqual(left_Rotate(0, 32), 0)

    def test_negative_shift(self):
        self.assertEqual(left_Rotate(123, -2), 916)
        self.assertEqual(left_Rotate(12345, -3), 12342)

    def test_shift_equal_to_bits(self):
        self.assertEqual(left_Rotate(123, 32), 15728643)
        self.assertEqual(left_Rotate(12345, 32), 12345)

    def test_shift_greater_than_bits(self):
        self.assertEqual(left_Rotate(123, 33), 126)
        self.assertEqual(left_Rotate(12345, 33), 12345)

    def test_negative_number(self):
        self.assertEqual(left_Rotate(-123, 2), -246)

    def test_large_number(self):
        self.assertEqual(left_Rotate(2147483647, 1), 2147483648)
