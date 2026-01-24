import unittest
from mbpp_799_code import left_Rotate

class TestLeftRotate(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(left_Rotate(10, 2), 40)
        self.assertEqual(left_Rotate(15, 1), 30)
        self.assertEqual(left_Rotate(8, 3), 120)

    def test_boundary_conditions(self):
        self.assertEqual(left_Rotate(0, 0), 0)
        self.assertEqual(left_Rotate(0, 32), 0)
        self.assertEqual(left_Rotate(2147483647, 1), 1073741824)

    def test_edge_cases(self):
        self.assertEqual(left_Rotate(2147483647, 32), 2147483647)
        self.assertEqual(left_Rotate(2147483647, 33), 2147483647)
        self.assertEqual(left_Rotate(-1, 1), -2147483648)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            left_Rotate("10", 2)
        with self.assertRaises(TypeError):
            left_Rotate(10, "2")
        with self.assertRaises(TypeError):
            left_Rotate("10", "2")
