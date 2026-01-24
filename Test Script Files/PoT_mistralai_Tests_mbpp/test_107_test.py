import unittest
from mbpp_107_code import count_Hexadecimal

class TestCountHexadecimal(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_Hexadecimal(10, 20), 5)
        self.assertEqual(count_Hexadecimal(30, 40), 10)
        self.assertEqual(count_Hexadecimal(50, 60), 15)

    def test_edge_case_min(self):
        self.assertEqual(count_Hexadecimal(0, 9), 0)
        self.assertEqual(count_Hexadecimal(1, 9), 1)
        self.assertEqual(count_Hexadecimal(10, 9), 1)

    def test_edge_case_max(self):
        self.assertEqual(count_Hexadecimal(15, 16), 1)
        self.assertEqual(count_Hexadecimal(15, 15), 0)
        self.assertEqual(count_Hexadecimal(15, 150), 1)

    def test_corner_case_large_input(self):
        self.assertEqual(count_Hexadecimal(1, 1000000), 666666)

    def test_corner_case_small_input(self):
        self.assertEqual(count_Hexadecimal(1, 10), 1)
