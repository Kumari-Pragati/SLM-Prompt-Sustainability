import unittest
from mbpp_799_code import left_Rotate

class TestLeftRotate(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(left_Rotate(16, 2), 64)

    def test_boundary_conditions(self):
        self.assertEqual(left_Rotate(0, 32), 0)
        self.assertEqual(left_Rotate(2147483647, 1), 2147483648)

    def test_edge_cases(self):
        self.assertEqual(left_Rotate(1, 32), 1)
        self.assertEqual(left_Rotate(2147483647, 0), 2147483647)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            left_Rotate("16", 2)
        with self.assertRaises(TypeError):
            left_Rotate(16, "2")
        with self.assertRaises(ValueError):
            left_Rotate(16, -2)
        with self.assertRaises(ValueError):
            left_Rotate(16, 33)
