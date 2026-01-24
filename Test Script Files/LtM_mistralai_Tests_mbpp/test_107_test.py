import unittest
from mbpp_107_code import count_Hexadecimal

class TestCountHexadecimal(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(count_Hexadecimal(10, 15), 6)
        self.assertEqual(count_Hexadecimal(16, 25), 10)
        self.assertEqual(count_Hexadecimal(26, 35), 0)

    def test_edge_and_boundary(self):
        self.assertEqual(count_Hexadecimal(0, 9), 0)
        self.assertEqual(count_Hexadecimal(10, 0), 0)
        self.assertEqual(count_Hexadecimal(16, 16), 1)
        self.assertEqual(count_Hexadecimal(15, 15), 1)
        self.assertEqual(count_Hexadecimal(17, 17), 0)
        self.assertEqual(count_Hexadecimal(255, 255), 16)
        self.assertEqual(count_Hexadecimal(256, 256), 0)
        self.assertEqual(count_Hexadecimal(1073741823, 1073741823), 1)

    def test_complex(self):
        self.assertEqual(count_Hexadecimal(10, 20), 6)
        self.assertEqual(count_Hexadecimal(100, 110), 10)
        self.assertEqual(count_Hexadecimal(1000, 1100), 25)
        self.assertEqual(count_Hexadecimal(10000, 11000), 250)
        self.assertEqual(count_Hexadecimal(100000, 110000), 2500)
        self.assertEqual(count_Hexadecimal(1000000, 1100000), 25000)
        self.assertEqual(count_Hexadecimal(10000000, 11000000), 250000)
        self.assertEqual(count_Hexadecimal(100000000, 110000000), 2500000)
