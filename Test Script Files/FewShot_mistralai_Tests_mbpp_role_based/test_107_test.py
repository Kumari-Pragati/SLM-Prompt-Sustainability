import unittest
from mbpp_107_code import count_Hexadecimal

class TestCountHexadecimal(unittest.TestCase):
    def test_count_valid_range(self):
        self.assertEqual(count_Hexadecimal(10, 20), 11)
        self.assertEqual(count_Hexadecimal(20, 30), 10)
        self.assertEqual(count_Hexadecimal(30, 40), 9)

    def test_count_single_hex_number(self):
        self.assertEqual(count_Hexadecimal(10, 10), 1)
        self.assertEqual(count_Hexadecimal(15, 15), 1)
        self.assertEqual(count_Hexadecimal(16, 16), 1)

    def test_count_large_hex_number(self):
        self.assertEqual(count_Hexadecimal(100, 100), 26)
        self.assertEqual(count_Hexadecimal(1000, 1000), 256)
        self.assertEqual(count_Hexadecimal(10000, 10000), 255)

    def test_count_negative_number(self):
        self.assertEqual(count_Hexadecimal(-10, -1), 0)

    def test_count_zero(self):
        self.assertEqual(count_Hexadecimal(0, 0), 0)

    def test_count_out_of_range(self):
        self.assertEqual(count_Hexadecimal(0, 9), 0)
        self.assertEqual(count_Hexadecimal(16, 17), 0)
        self.assertEqual(count_Hexadecimal(16, 10), 0)
        self.assertEqual(count_Hexadecimal(10, 16), 0)
        self.assertEqual(count_Hexadecimal(15, 10), 0)
