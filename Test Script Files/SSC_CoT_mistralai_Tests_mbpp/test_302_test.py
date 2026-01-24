import unittest
from mbpp_302_code import set_Bit_Number

class TestSetBitNumber(unittest.TestCase):

    def test_normal_inputs(self):
        self.assertEqual(set_Bit_Number(1), 2)
        self.assertEqual(set_Bit_Number(10), 16)
        self.assertEqual(set_Bit_Number(32), 64)
        self.assertEqual(set_Bit_Number(128), 256)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(set_Bit_Number(0), 0)
        self.assertEqual(set_Bit_Number(127), 255)
        self.assertEqual(set_Bit_Number(255), 256)
        self.assertEqual(set_Bit_Number(256), 512)
        self.assertEqual(set_Bit_Number(511), 1024)
        self.assertEqual(set_Bit_Number(1023), 2048)
        self.assertEqual(set_Bit_Number(1024), 2048)
        self.assertEqual(set_Bit_Number(2047), 4096)
        self.assertEqual(set_Bit_Number(4095), 8192)
        self.assertEqual(set_Bit_Number(4096), 8192)
