import unittest
from mbpp_302_code import set_Bit_Number

class TestSetBitNumber(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(set_Bit_Number(0), 0)
        self.assertEqual(set_Bit_Number(1), 1)
        self.assertEqual(set_Bit_Number(2), 2)
        self.assertEqual(set_Bit_Number(3), 4)
        self.assertEqual(set_Bit_Number(4), 4)
        self.assertEqual(set_Bit_Number(5), 8)
        self.assertEqual(set_Bit_Number(6), 8)
        self.assertEqual(set_Bit_Number(7), 8)
        self.assertEqual(set_Bit_Number(8), 8)

    def test_edge_conditions(self):
        self.assertEqual(set_Bit_Number(9), 16)
        self.assertEqual(set_Bit_Number(10), 16)
        self.assertEqual(set_Bit_Number(11), 16)
        self.assertEqual(set_Bit_Number(12), 16)
        self.assertEqual(set_Bit_Number(13), 16)
        self.assertEqual(set_Bit_Number(14), 16)
        self.assertEqual(set_Bit_Number(15), 16)
        self.assertEqual(set_Bit_Number(16), 16)

    def test_complex_cases(self):
        self.assertEqual(set_Bit_Number(17), 32)
        self.assertEqual(set_Bit_Number(18), 32)
        self.assertEqual(set_Bit_Number(19), 32)
        self.assertEqual(set_Bit_Number(20), 32)
        self.assertEqual(set_Bit_Number(21), 32)
        self.assertEqual(set_Bit_Number(22), 32)
        self.assertEqual(set_Bit_Number(23), 32)
        self.assertEqual(set_Bit_Number(24), 32)
