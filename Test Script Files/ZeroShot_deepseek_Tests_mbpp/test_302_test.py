import unittest
from mbpp_302_code import set_Bit_Number

class TestSetBitNumber(unittest.TestCase):

    def test_set_Bit_Number_with_zero(self):
        self.assertEqual(set_Bit_Number(0), 0)

    def test_set_Bit_Number_with_positive_numbers(self):
        self.assertEqual(set_Bit_Number(1), 1)
        self.assertEqual(set_Bit_Number(2), 2)
        self.assertEqual(set_Bit_Number(4), 4)
        self.assertEqual(set_Bit_Number(8), 8)
        self.assertEqual(set_Bit_Number(16), 16)
        self.assertEqual(set_Bit_Number(32), 32)
        self.assertEqual(set_Bit_Number(64), 64)
        self.assertEqual(set_Bit_Number(128), 128)
        self.assertEqual(set_Bit_Number(256), 256)
        self.assertEqual(set_Bit_Number(512), 512)
        self.assertEqual(set_Bit_Number(1024), 1024)
        self.assertEqual(set_Bit_Number(2048), 2048)
        self.assertEqual(set_Bit_Number(4096), 4096)
        self.assertEqual(set_Bit_Number(8192), 8192)
        self.assertEqual(set_Bit_Number(16384), 16384)
        self.assertEqual(set_Bit_Number(32768), 32768)
        self.assertEqual(set_Bit_Number(65536), 65536)
        self.assertEqual(set_Bit_Number(131072), 131072)
        self.assertEqual(set_Bit_Number(262144), 262144)
        self.assertEqual(set_Bit_Number(524288), 524288)
        self.assertEqual(set_Bit_Number(1048576), 1048576)
        self.assertEqual(set_Bit_Number(2097152), 2097152)
        self.assertEqual(set_Bit_Number(4194304), 4194304)
        self.assertEqual(set_Bit_Number(8388608), 8388608)
        self.assertEqual(set_Bit_Number(16777216), 16777216)
        self.assertEqual(set_Bit_Number(33554432), 33554432)
        self.assertEqual(set_Bit_Number(67108864), 67108864)
        self.assertEqual(set_Bit_Number(134217728), 134217728)
        self.assertEqual(set_Bit_Number(268435456), 268435456)
        self.assertEqual(set_Bit_Number(536870912), 536870912)
        self.assertEqual(set_Bit_Number(1073741824), 1073741824)
