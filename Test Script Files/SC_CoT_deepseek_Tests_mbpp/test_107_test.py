import unittest

from mbpp_107_code import count_Hexadecimal

class TestCountHexadecimal(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_Hexadecimal(10, 15), 2)
        self.assertEqual(count_Hexadecimal(0, 1), 0)
        self.assertEqual(count_Hexadecimal(16, 20), 1)

    def test_boundary_conditions(self):
        self.assertEqual(count_Hexadecimal(10, 10), 1)
        self.assertEqual(count_Hexadecimal(15, 15), 1)
        self.assertEqual(count_Hexadecimal(16, 16), 1)

    def test_edge_cases(self):
        self.assertEqual(count_Hexadecimal(9, 10), 1)
        self.assertEqual(count_Hexadecimal(17, 20), 1)
        self.assertEqual(count_Hexadecimal(0, -1), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_Hexadecimal("10", 15)
        with self.assertRaises(TypeError):
            count_Hexadecimal(10, "15")
        with self.assertRaises(ValueError):
            count_Hexadecimal(20, 10)
