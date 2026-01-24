import unittest
from mbpp_107_code import count_Hexadecimal

class TestCountHexadecimal(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(count_Hexadecimal(10, 15), 6)
        self.assertEqual(count_Hexadecimal(15, 20), 0)
        self.assertEqual(count_Hexadecimal(10, 10), 0)
        self.assertEqual(count_Hexadecimal(15, 15), 1)

    def test_edge_cases(self):
        self.assertEqual(count_Hexadecimal(9, 10), 0)
        self.assertEqual(count_Hexadecimal(16, 20), 0)
        self.assertEqual(count_Hexadecimal(0, 10), 0)
        self.assertEqual(count_Hexadecimal(15, 16), 1)

    def test_complex_inputs(self):
        self.assertEqual(count_Hexadecimal(10, 20), 6)
        self.assertEqual(count_Hexadecimal(15, 25), 1)
        self.assertEqual(count_Hexadecimal(10, 30), 6)
