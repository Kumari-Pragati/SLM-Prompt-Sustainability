import unittest
from mbpp_107_code import count_Hexadecimal

class TestCountHexadecimal(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_Hexadecimal(10, 15), 2)
        self.assertEqual(count_Hexadecimal(16, 20), 1)
        self.assertEqual(count_Hexadecimal(100, 110), 2)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_Hexadecimal(0, 10), 1)
        self.assertEqual(count_Hexadecimal(15, 15), 1)
        self.assertEqual(count_Hexadecimal(16, 16), 1)
        self.assertEqual(count_Hexadecimal(17, 20), 0)

    def test_corner_cases(self):
        self.assertEqual(count_Hexadecimal(10, 16), 2)
        self.assertEqual(count_Hexadecimal(17, 20), 0)
        self.assertEqual(count_Hexadecimal(30, 40), 0)
        self.assertEqual(count_Hexadecimal(100, 105), 1)
