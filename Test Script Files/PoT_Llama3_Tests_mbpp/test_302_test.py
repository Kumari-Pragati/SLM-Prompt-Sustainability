import unittest
from mbpp_302_code import set_Bit_Number

class TestSetBitNumber(unittest.TestCase):

    def test_set_Bit_Number_typical(self):
        self.assertEqual(set_Bit_Number(1), 1)
        self.assertEqual(set_Bit_Number(2), 2)
        self.assertEqual(set_Bit_Number(3), 4)
        self.assertEqual(set_Bit_Number(4), 4)
        self.assertEqual(set_Bit_Number(5), 8)

    def test_set_Bit_Number_edge(self):
        self.assertEqual(set_Bit_Number(0), 0)
        self.assertEqual(set_Bit_Number(1), 1)
        self.assertEqual(set_Bit_Number(2**31 - 1), 2**31 - 1)

    def test_set_Bit_Number_corner(self):
        self.assertEqual(set_Bit_Number(2**31), 2**31)
        self.assertEqual(set_Bit_Number(2**32 - 1), 2**32 - 1)
