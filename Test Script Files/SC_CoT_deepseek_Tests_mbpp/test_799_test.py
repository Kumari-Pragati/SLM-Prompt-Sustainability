import unittest
from mbpp_799_code import left_Rotate

class TestLeftRotate(unittest.TestCase):
    
    def test_typical_cases(self):
        self.assertEqual(left_Rotate(10, 2), 40)
        self.assertEqual(left_Rotate(15, 1), 30)
        self.assertEqual(left_Rotate(0, 5), 0)

    def test_boundary_conditions(self):
        self.assertEqual(left_Rotate(2**32 - 1, 1), 2**31)
        self.assertEqual(left_Rotate(2**31 - 1, 1), 2**30 - 1)

    def test_edge_cases(self):
        self.assertEqual(left_Rotate(2**32, 0), 2**32)
        self.assertEqual(left_Rotate(2**32, 32), 0)
        self.assertEqual(left_Rotate(2**32 - 1, 33), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            left_Rotate("10", 2)
        with self.assertRaises(TypeError):
            left_Rotate(10, "2")
        with self.assertRaises(ValueError):
            left_Rotate(10, -2)
        with self.assertRaises(ValueError):
            left_Rotate(10, 33)
