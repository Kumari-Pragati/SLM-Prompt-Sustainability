import unittest
from mbpp_107_code import count_Hexadecimal

class TestCountHexadecimal(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count_Hexadecimal(10, 20), 2)

    def test_edge_case_start(self):
        self.assertEqual(count_Hexadecimal(10, 10), 0)

    def test_edge_case_end(self):
        self.assertEqual(count_Hexadecimal(15, 15), 1)

    def test_edge_case_range(self):
        self.assertEqual(count_Hexadecimal(10, 15), 1)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            count_Hexadecimal("10", "20")

    def test_invalid_input_range(self):
        with self.assertRaises(ValueError):
            count_Hexadecimal(10, 5)
