import unittest
from mbpp_107_code import count_Hexadecimal

class TestCountHexadecimal(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(count_Hexadecimal(10, 20), 11)
        self.assertEqual(count_Hexadecimal(20, 30), 15)
        self.assertEqual(count_Hexadecimal(30, 40), 15)
        self.assertEqual(count_Hexadecimal(40, 50), 15)
        self.assertEqual(count_Hexadecimal(50, 60), 15)
        self.assertEqual(count_Hexadecimal(60, 70), 15)
        self.assertEqual(count_Hexadecimal(70, 80), 15)
        self.assertEqual(count_Hexadecimal(80, 90), 15)
        self.assertEqual(count_Hexadecimal(90, 100), 15)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_Hexadecimal(0, 9), 0)
        self.assertEqual(count_Hexadecimal(1, 9), 1)
        self.assertEqual(count_Hexadecimal(10, 0), 0)
        self.assertEqual(count_Hexadecimal(10, 1), 1)
        self.assertEqual(count_Hexadecimal(10, 10), 1)
        self.assertEqual(count_Hexadecimal(16, 16), 1)
        self.assertEqual(count_Hexadecimal(15, 16), 1)
        self.assertEqual(count_Hexadecimal(16, 15), 0)
        self.assertEqual(count_Hexadecimal(16, 17), 1)
        self.assertEqual(count_Hexadecimal(17, 16), 0)
        self.assertEqual(count_Hexadecimal(17, 17), 1)
        self.assertEqual(count_Hexadecimal(17, 18), 1)
        self.assertEqual(count_Hexadecimal(18, 17), 0)
        self.assertEqual(count_Hexadecimal(18, 18), 1)
        self.assertEqual(count_Hexadecimal(18, 19), 1)
        self.assertEqual(count_Hexadecimal(19, 18), 0)
        self.assertEqual(count_Hexadecimal(19, 19), 1)

    def test_special_cases(self):
        self.assertEqual(count_Hexadecimal(10, 1000000), 1000000)
        self.assertEqual(count_Hexadecimal(1000000, 1000000), 1000000)
        self.assertEqual(count_Hexadecimal(1000000000, 1000000000), 1000000000)
