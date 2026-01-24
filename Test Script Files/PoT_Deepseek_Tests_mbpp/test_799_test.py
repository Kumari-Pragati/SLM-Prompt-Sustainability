import unittest
from mbpp_799_code import left_Rotate

class TestLeftRotate(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(left_Rotate(10, 2), 40)
        self.assertEqual(left_Rotate(15, 1), 30)
        self.assertEqual(left_Rotate(8, 3), 120)

    def test_edge_cases(self):
        self.assertEqual(left_Rotate(0, 10), 0)
        self.assertEqual(left_Rotate(2147483647, 1), 2147483648)

    def test_boundary_conditions(self):
        self.assertEqual(left_Rotate(2147483648, 0), 2147483648)
        self.assertEqual(left_Rotate(2147483648, 31), 0)
        self.assertEqual(left_Rotate(2147483648, 32), 2147483648)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            left_Rotate("10", 2)
        with self.assertRaises(TypeError):
            left_Rotate(10, "2")
        with self.assertRaises(ValueError):
            left_Rotate(10, -2)
        with self.assertRaises(ValueError):
            left_Rotate(10, 33)
