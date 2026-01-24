import unittest
from mbpp_127_code import multiply_int

class TestMultiplyInt(unittest.TestCase):

    def test_normal_inputs(self):
        self.assertEqual(multiply_int(2, 3), 6)
        self.assertEqual(multiply_int(-3, 4), -12)
        self.assertEqual(multiply_int(0, 5), 0)
        self.assertEqual(multiply_int(7, 0), 0)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(multiply_int(2, -1), -2)
        self.assertEqual(multiply_int(-2, -1), 2)
        self.assertEqual(multiply_int(1, -1), -1)
        self.assertEqual(multiply_int(-1, -1), 1)
        self.assertEqual(multiply_int(2, 10), 20)
        self.assertEqual(multiply_int(-2, 10), -20)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, multiply_int, "x", 3)
        self.assertRaises(TypeError, multiply_int, 2, "y")
