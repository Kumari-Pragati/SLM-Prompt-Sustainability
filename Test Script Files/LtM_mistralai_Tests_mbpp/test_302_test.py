import unittest
from mbpp_302_code import set_Bit_Number

class TestSetBitNumber(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(set_Bit_Number(1), 2)
        self.assertEqual(set_Bit_Number(3), 4)
        self.assertEqual(set_Bit_Number(7), 8)

    def test_edge_cases(self):
        self.assertEqual(set_Bit_Number(0), 0)
        self.assertEqual(set_Bit_Number(16), 16)
        self.assertEqual(set_Bit_Number(32), 32)
        self.assertEqual(set_Bit_Number(64), 64)

    def test_complex_cases(self):
        self.assertEqual(set_Bit_Number(125), 128)
        self.assertEqual(set_Bit_Number(126), 128)
        self.assertEqual(set_Bit_Number(127), 128)
        self.assertEqual(set_Bit_Number(128), 128)
        self.assertEqual(set_Bit_Number(129), 128)
        self.assertEqual(set_Bit_Number(255), 256)
        self.assertEqual(set_Bit_Number(256), 256)
        self.assertEqual(set_Bit_Number(511), 512)
        self.assertEqual(set_Bit_Number(512), 512)
        self.assertEqual(set_Bit_Number(1023), 1024)
        self.assertEqual(set_Bit_Number(1024), 1024)
