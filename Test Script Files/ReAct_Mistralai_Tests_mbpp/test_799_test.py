import unittest
from mbpp_799_code import left_Rotate

class TestLeftRotate(unittest.TestCase):

    def test_left_rotate_positive_numbers(self):
        self.assertEqual(left_Rotate(12, 2), 96)
        self.assertEqual(left_Rotate(100, 3), 3200)
        self.assertEqual(left_Rotate(1000000, 1), 1000000)

    def test_left_rotate_negative_numbers(self):
        self.assertEqual(left_Rotate(-12, 2), -3)
        self.assertEqual(left_Rotate(-100, 3), -3200)
        self.assertEqual(left_Rotate(-1000000, 1), -1000000)

    def test_left_rotate_zero(self):
        self.assertEqual(left_Rotate(0, 2), 0)

    def test_left_rotate_edge_cases(self):
        self.assertEqual(left_Rotate(1, 0), 1)
        self.assertEqual(left_Rotate(1, 31), 2147483648)
        self.assertEqual(left_Rotate(-1, 0), -1)
        self.assertEqual(left_Rotate(-1, 31), -2147483648)

    def test_left_rotate_large_numbers(self):
        large_num = (1 << 31) - 1
        self.assertEqual(left_Rotate(large_num, 1), large_num)
        self.assertEqual(left_Rotate(large_num, 31), 0)

    def test_left_rotate_invalid_d(self):
        with self.assertRaises(ValueError):
            left_Rotate(1, 32)
        with self.assertRaises(ValueError):
            left_Rotate(1, -1)
