import unittest
from mbpp_799_code import left_Rotate

class TestLeftRotate(unittest.TestCase):
    def test_left_rotate(self):
        self.assertEqual(left_Rotate(1, 1), 2)
        self.assertEqual(left_Rotate(1, 2), 4)
        self.assertEqual(left_Rotate(1, 3), 1)
        self.assertEqual(left_Rotate(2, 1), 4)
        self.assertEqual(left_Rotate(2, 2), 1)
        self.assertEqual(left_Rotate(2, 3), 2)
        self.assertEqual(left_Rotate(0, 1), 0)
        self.assertEqual(left_Rotate(0, 2), 0)
        self.assertEqual(left_Rotate(0, 3), 0)
        self.assertEqual(left_Rotate(1, 0), 1)
        self.assertEqual(left_Rotate(2, 0), 2)
        self.assertEqual(left_Rotate(0, 0), 0)
