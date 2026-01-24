import unittest
from107_code import count_Hexadecimal

class TestCountHexadecimal(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_Hexadecimal(10, 20), 11)
        self.assertEqual(count_Hexadecimal(20, 30), 15)
        self.assertEqual(count_Hexadecimal(30, 40), 15)
        self.assertEqual(count_Hexadecimal(40, 50), 15)
        self.assertEqual(count_Hexadecimal(50, 60), 15)
        self.assertEqual(count_Hexadecimal(60, 70), 15)
        self.assertEqual(count_Hexadecimal(70, 80), 15)
        self.assertEqual(count_Hexadecimal(80, 90), 15)
        self.assertEqual(count_Hexadecimal(90, 100), 15)

    def test_edge_cases(self):
        self.assertEqual(count_Hexadecimal(0, 10), 0)
        self.assertEqual(count_Hexadecimal(10, 0), 0)
        self.assertEqual(count_Hexadecimal(10, 10), 1)
        self.assertEqual(count_Hexadecimal(15, 15), 1)
        self.assertEqual(count_Hexadecimal(16, 16), 1)
        self.assertEqual(count_Hexadecimal(17, 17), 1)
        self.assertEqual(count_Hexadecimal(255, 255), 16)
        self.assertEqual(count_Hexadecimal(256, 256), 0)
        self.assertEqual(count_Hexadecimal(1000, 1000), 0)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, count_Hexadecimal, 'a', 'b')
        self.assertRaises(TypeError, count_Hexadecimal, 10, 'b')
        self.assertRaises(TypeError, count_Hexadecimal, 'a', 10)
        self.assertRaises(ValueError, count_Hexadecimal, -10, 20)
        self.assertRaises(ValueError, count_Hexadecimal, 10, -20)
