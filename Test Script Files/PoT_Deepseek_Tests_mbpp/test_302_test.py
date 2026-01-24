import unittest
from mbpp_302_code import set_Bit_Number

class TestSetBitNumber(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(set_Bit_Number(0), 0)
        self.assertEqual(set_Bit_Number(1), 1)
        self.assertEqual(set_Bit_Number(2), 2)
        self.assertEqual(set_Bit_Number(4), 4)
        self.assertEqual(set_Bit_Number(8), 8)

    def test_edge_cases(self):
        self.assertEqual(set_Bit_Number(1024), 1024)
        self.assertEqual(set_Bit_Number(2048), 2048)

    def test_boundary_cases(self):
        self.assertEqual(set_Bit_Number(512), 512)
        self.assertEqual(set_Bit_Number(1023), 512)
        self.assertEqual(set_Bit_Number(2047), 1024)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            set_Bit_Number('invalid')
        with self.assertRaises(ValueError):
            set_Bit_Number(-1)
