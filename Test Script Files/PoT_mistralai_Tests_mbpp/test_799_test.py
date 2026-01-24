import unittest
from mbpp_799_code import left_Rotate

class TestLeftRotate(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(left_Rotate(12, 2), 96)
        self.assertEqual(left_Rotate(255, 1), 528)
        self.assertEqual(left_Rotate(1073741823, 30), 1)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(left_Rotate(0, 32), 0)
        self.assertEqual(left_Rotate(4294967295, 1), 0)
        self.assertEqual(left_Rotate(4294967295, 31), 4294967295 << 1)
        self.assertEqual(left_Rotate(-1, 1), -2)
        self.assertEqual(left_Rotate(-1, 31), -2147483648)
