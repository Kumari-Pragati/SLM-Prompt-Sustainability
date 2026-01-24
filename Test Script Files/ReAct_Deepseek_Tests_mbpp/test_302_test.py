import unittest
from mbpp_302_code import set_Bit_Number

class TestSetBitNumber(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(set_Bit_Number(0), 0)
        self.assertEqual(set_Bit_Number(1), 1)
        self.assertEqual(set_Bit_Number(2), 2)
        self.assertEqual(set_Bit_Number(4), 4)
        self.assertEqual(set_Bit_Number(8), 8)
        self.assertEqual(set_Bit_Number(16), 16)

    def test_edge_cases(self):
        self.assertEqual(set_Bit_Number(32), 32)
        self.assertEqual(set_Bit_Number(64), 64)
        self.assertEqual(set_Bit_Number(128), 128)
        self.assertEqual(set_Bit_Number(256), 256)
        self.assertEqual(set_Bit_Number(512), 512)

    def test_large_numbers(self):
        self.assertEqual(set_Bit_Number(1024), 1024)
        self.assertEqual(set_Bit_Number(2048), 2048)
        self.assertEqual(set_Bit_Number(4096), 4096)
        self.assertEqual(set_Bit_Number(8192), 8192)
        self.assertEqual(set_Bit_Number(16384), 16384)

    def test_negative_numbers(self):
        self.assertEqual(set_Bit_Number(-1), 0)
        self.assertEqual(set_Bit_Number(-2), 0)
        self.assertEqual(set_Bit_Number(-4), 0)
        self.assertEqual(set_Bit_Number(-8), 0)
        self.assertEqual(set_Bit_Number(-16), 0)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            set_Bit_Number(3.5)
