import unittest
from mbpp_799_code import left_Rotate

class TestLeftRotate(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(left_Rotate(12, 2), 48)
        self.assertEqual(left_Rotate(100, 3), 323)
        self.assertEqual(left_Rotate(-12, 2), -288)

    def test_edge_cases(self):
        self.assertEqual(left_Rotate(0, 0), 0)
        self.assertEqual(left_Rotate(0, 32), 0)
        self.assertEqual(left_Rotate(1, 0), 1)
        self.assertEqual(left_Rotate(1, 31), 2147483648)
        self.assertEqual(left_Rotate(-1, 0), -1)
        self.assertEqual(left_Rotate(-1, 31), -2147483647)

    def test_negative_d(self):
        self.assertEqual(left_Rotate(12, -2), 604800)
        self.assertEqual(left_Rotate(-12, -2), 604800)

    def test_d_greater_than_INT_BITS(self):
        self.assertEqual(left_Rotate(12, 33), 18446744073709551616)
        self.assertEqual(left_Rotate(-12, 33), 18446744073709551616)
