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
        self.assertEqual(set_Bit_Number(1), 1)
        self.assertEqual(set_Bit_Number(3), 4)
        self.assertEqual(set_Bit_Number(7), 8)
        self.assertEqual(set_Bit_Number(15), 16)
        self.assertEqual(set_Bit_Number(31), 32)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            set_Bit_Number('a')
        with self.assertRaises(TypeError):
            set_Bit_Number(None)
        with self.assertRaises(TypeError):
            set_Bit_Number([])
        with self.assertRaises(TypeError):
            set_Bit_Number({})
