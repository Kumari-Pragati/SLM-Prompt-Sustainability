import unittest
from mbpp_107_code import count_Hexadecimal

class TestCountHexadecimal(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(count_Hexadecimal(10, 15), 6)
        self.assertEqual(count_Hexadecimal(10, 20), 6)

    def test_edge_cases(self):
        self.assertEqual(count_Hexadecimal(9, 10), 0)
        self.assertEqual(count_Hexadecimal(15, 16), 1)
        self.assertEqual(count_Hexadecimal(15, 20), 6)

    def test_boundary_cases(self):
        self.assertEqual(count_Hexadecimal(10, 10), 1)
        self.assertEqual(count_Hexadecimal(15, 15), 1)
        self.assertEqual(count_Hexadecimal(10, 20), 6)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_Hexadecimal('a', 10)
        with self.assertRaises(TypeError):
            count_Hexadecimal(10, 'b')

    def test_special_cases(self):
        self.assertEqual(count_Hexadecimal(10, 10), 1)
        self.assertEqual(count_Hexadecimal(15, 15), 1)
        self.assertEqual(count_Hexadecimal(10, 20), 6)
