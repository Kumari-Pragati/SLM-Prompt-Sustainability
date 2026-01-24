import unittest
from mbpp_107_code import count_Hexadecimal

class TestCountHexadecimal(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count_Hexadecimal(10, 15), 3)

    def test_boundary_conditions(self):
        self.assertEqual(count_Hexadecimal(0, 10), 1)
        self.assertEqual(count_Hexadecimal(16, 20), 1)
        self.assertEqual(count_Hexadecimal(10, 16), 2)

    def test_edge_conditions(self):
        self.assertEqual(count_Hexadecimal(10, 10), 1)
        self.assertEqual(count_Hexadecimal(15, 15), 1)
        self.assertEqual(count_Hexadecimal(16, 16), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_Hexadecimal("10", 15)
        with self.assertRaises(TypeError):
            count_Hexadecimal(10, "15")
        with self.assertRaises(ValueError):
            count_Hexadecimal(15, 10)
