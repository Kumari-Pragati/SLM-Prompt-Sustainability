import unittest
from mbpp_127_code import multiply_int

class TestMultiplyInt(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(multiply_int(2, 3), 6)
        self.assertEqual(multiply_int(-2, 3), -6)
        self.assertEqual(multiply_int(2, -3), -6)
        self.assertEqual(multiply_int(-2, -3), 6)

    def test_edge_cases(self):
        self.assertEqual(multiply_int(0, 100), 0)
        self.assertEqual(multiply_int(100, 0), 0)
        self.assertEqual(multiply_int(0, 0), 0)

    def test_boundary_cases(self):
        self.assertEqual(multiply_int(1, 1000), 1000)
        self.assertEqual(multiply_int(-1, 1000), -1000)
        self.assertEqual(multiply_int(1000, 1), 1000)
        self.assertEqual(multiply_int(-1000, 1), -1000)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            multiply_int(2, '3')
        with self.assertRaises(TypeError):
            multiply_int('2', 3)
        with self.assertRaises(TypeError):
            multiply_int('2', '3')
