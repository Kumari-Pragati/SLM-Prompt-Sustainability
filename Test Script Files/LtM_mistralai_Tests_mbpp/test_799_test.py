import unittest
from mbpp_799_code import left_Rotate

class TestLeftRotate(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(left_Rotate(12, 2), 96)
        self.assertEqual(left_Rotate(255, 1), 528)
        self.assertEqual(left_Rotate(10, 3), 160)

    def test_edge_and_boundary(self):
        self.assertEqual(left_Rotate(0, 1), 2)
        self.assertEqual(left_Rotate(1, 0), 256)
        self.assertEqual(left_Rotate(2147483647, 1), 2)
        self.assertEqual(left_Rotate(2147483647, 31), 2147483648)

    def test_complex(self):
        self.assertEqual(left_Rotate(123456789, 10), 1234567890)
        self.assertEqual(left_Rotate(1234567890, 31), 18446744073709551610)
        self.assertEqual(left_Rotate(1234567890, 32), 1234567890)
