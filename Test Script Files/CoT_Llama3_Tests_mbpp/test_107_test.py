import unittest
from mbpp_107_code import count_Hexadecimal

class TestCountHexadecimal(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Hexadecimal(10, 15), 5)

    def test_edge_case_L_equal_R(self):
        self.assertEqual(count_Hexadecimal(10, 10), 1)

    def test_edge_case_R_equal_L_plus_one(self):
        self.assertEqual(count_Hexadecimal(15, 15), 1)

    def test_edge_case_L_greater_than_R(self):
        self.assertEqual(count_Hexadecimal(20, 15), 0)

    def test_edge_case_R_greater_than_L_plus_one(self):
        self.assertEqual(count_Hexadecimal(15, 20), 0)

    def test_invalid_input_type_L(self):
        with self.assertRaises(TypeError):
            count_Hexadecimal('a', 15)

    def test_invalid_input_type_R(self):
        with self.assertRaises(TypeError):
            count_Hexadecimal(10, 'a')

    def test_invalid_input_type_L_and_R(self):
        with self.assertRaises(TypeError):
            count_Hexadecimal('a', 'b')
