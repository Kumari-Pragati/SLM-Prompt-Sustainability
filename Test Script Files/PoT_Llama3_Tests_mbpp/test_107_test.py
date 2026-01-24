import unittest
from mbpp_107_code import count_Hexadecimal

class TestCountHexadecimal(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_Hexadecimal(10, 15), 6)

    def test_edge_case_L(self):
        self.assertEqual(count_Hexadecimal(10, 10), 0)

    def test_edge_case_R(self):
        self.assertEqual(count_Hexadecimal(15, 15), 1)

    def test_edge_case_L_R(self):
        self.assertEqual(count_Hexadecimal(10, 15), 6)

    def test_tricky_case(self):
        self.assertEqual(count_Hexadecimal(16, 20), 2)

    def test_tricky_case_L(self):
        self.assertEqual(count_Hexadecimal(16, 16), 1)

    def test_tricky_case_R(self):
        self.assertEqual(count_Hexadecimal(20, 20), 2)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_Hexadecimal('a', 15)
