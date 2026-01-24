import unittest
from mbpp_799_code import left_Rotate

class TestLeftRotate(unittest.TestCase):
    def test_left_rotate_positive_numbers(self):
        self.assertEqual(left_Rotate(10, 2), 20)

    def test_left_rotate_negative_numbers(self):
        self.assertEqual(left_Rotate(-10, 2), -20)

    def test_left_rotate_zero(self):
        self.assertEqual(left_Rotate(0, 0), 0)

    def test_left_rotate_max_value(self):
        self.assertEqual(left_Rotate(2**31 - 1, 1), 2**31 - 2**30)

    def test_left_rotate_max_value_shifted_to_max(self):
        self.assertEqual(left_Rotate(2**31 - 1, 31), 2**31 - 2**30)

    def test_left_rotate_max_value_shifted_to_zero(self):
        self.assertEqual(left_Rotate(2**31 - 1, 0), 2**31 - 1)

    def test_left_rotate_max_value_shifted_to_negative(self):
        self.assertEqual(left_Rotate(2**31 - 1, -1), 2**31 - 2**30)
