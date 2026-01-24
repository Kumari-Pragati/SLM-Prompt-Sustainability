import unittest
from mbpp_302_code import set_Bit_Number

class TestSetBitNumber(unittest.TestCase):
    def test_set_bit_number_positive_integer(self):
        self.assertEqual(set_Bit_Number(5), 16)

    def test_set_bit_number_zero(self):
        self.assertEqual(set_Bit_Number(0), 0)

    def test_set_bit_number_negative_integer(self):
        self.assertEqual(set_Bit_Number(-5), 16)

    def test_set_bit_number_non_integer(self):
        with self.assertRaises(TypeError):
            set_Bit_Number("five")

    def test_set_bit_number_large_integer(self):
        self.assertEqual(set_Bit_Number(1024), 2048)

    def test_set_bit_number_max_integer(self):
        self.assertEqual(set_Bit_Number(2147483647), 2147483648)
