import unittest
from mbpp_127_code import multiply_int

class TestMultiplyInt(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(multiply_int(2, 3), 6)
        self.assertEqual(multiply_int(-2, 3), -6)
        self.assertEqual(multiply_int(3, -2), -6)
        self.assertEqual(multiply_int(0, 0), 0)
        self.assertEqual(multiply_int(1, 2), 1)
        self.assertEqual(multiply_int(2, 1), 2)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(multiply_int(2, 0), 0)
        self.assertEqual(multiply_int(-2, 0), 0)
        self.assertEqual(multiply_int(2, -0), 0)
        self.assertEqual(multiply_int(-2, -0), 0)
        self.assertEqual(multiply_int(1, 0), 0)
        self.assertEqual(multiply_int(-1, 0), 0)
        self.assertEqual(multiply_int(2, 1e9), 2 * 1e9)
        self.assertEqual(multiply_int(-2, 1e9), -2 * 1e9)
