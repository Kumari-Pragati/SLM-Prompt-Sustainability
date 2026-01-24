import unittest
from mbpp_799_code import left_Rotate

class TestLeftRotate(unittest.TestCase):
    def test_simple_rotate(self):
        self.assertEqual(left_Rotate(1, 1), 2)
        self.assertEqual(left_Rotate(2, 1), 4)
        self.assertEqual(left_Rotate(3, 1), 6)
        self.assertEqual(left_Rotate(4, 1), 8)
        self.assertEqual(left_Rotate(5, 1), 10)

    def test_rotate_to_INT_BITS(self):
        self.assertEqual(left_Rotate(1, 32), 2)
        self.assertEqual(left_Rotate(2, 32), 4)
        self.assertEqual(left_Rotate(3, 32), 6)
        self.assertEqual(left_Rotate(4, 32), 8)
        self.assertEqual(left_Rotate(5, 32), 10)

    def test_rotate_to_INT_BITS_plus_one(self):
        self.assertEqual(left_Rotate(1, 33), 2)
        self.assertEqual(left_Rotate(2, 33), 4)
        self.assertEqual(left_Rotate(3, 33), 6)
        self.assertEqual(left_Rotate(4, 33), 8)
        self.assertEqual(left_Rotate(5, 33), 10)

    def test_rotate_to_INT_BITS_minus_one(self):
        self.assertEqual(left_Rotate(1, 31), 2)
        self.assertEqual(left_Rotate(2, 31), 4)
        self.assertEqual(left_Rotate(3, 31), 6)
        self.assertEqual(left_Rotate(4, 31), 8)
        self.assertEqual(left_Rotate(5, 31), 10)

    def test_rotate_to_INT_BITS_minus_two(self):
        self.assertEqual(left_Rotate(1, 30), 2)
        self.assertEqual(left_Rotate(2, 30), 4)
        self.assertEqual(left_Rotate(3, 30), 6)
        self.assertEqual(left_Rotate(4, 30), 8)
        self.assertEqual(left_Rotate(5, 30), 10)
