import unittest
from mbpp_302_code import set_Bit_Number

class TestSetBitNumber(unittest.TestCase):
    def test_set_Bit_Number_zero(self):
        self.assertEqual(set_Bit_Number(0), 0)

    def test_set_Bit_Number_positive(self):
        self.assertEqual(set_Bit_Number(1), 1)
        self.assertEqual(set_Bit_Number(2), 2)
        self.assertEqual(set_Bit_Number(3), 4)
        self.assertEqual(set_Bit_Number(4), 4)
        self.assertEqual(set_Bit_Number(5), 8)
        self.assertEqual(set_Bit_Number(6), 8)
        self.assertEqual(set_Bit_Number(7), 8)
        self.assertEqual(set_Bit_Number(8), 8)

    def test_set_Bit_Number_negative(self):
        self.assertEqual(set_Bit_Number(-1), 1)
        self.assertEqual(set_Bit_Number(-2), 2)
        self.assertEqual(set_Bit_Number(-3), 4)
        self.assertEqual(set_Bit_Number(-4), 4)
        self.assertEqual(set_Bit_Number(-5), 8)
        self.assertEqual(set_Bit_Number(-6), 8)
        self.assertEqual(set_Bit_Number(-7), 8)
        self.assertEqual(set_Bit_Number(-8), 8)

    def test_set_Bit_Number_large(self):
        self.assertEqual(set_Bit_Number(1024), 1024)

    def test_set_Bit_Number_invalid(self):
        with self.assertRaises(TypeError):
            set_Bit_Number('a')
