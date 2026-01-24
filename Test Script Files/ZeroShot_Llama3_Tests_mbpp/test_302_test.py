import unittest
from mbpp_302_code import set_Bit_Number

class TestSetBitNumber(unittest.TestCase):

    def test_set_Bit_Number_zero(self):
        self.assertEqual(set_Bit_Number(0), 0)

    def test_set_Bit_Number_one(self):
        self.assertEqual(set_Bit_Number(1), 1)

    def test_set_Bit_Number_two(self):
        self.assertEqual(set_Bit_Number(2), 2)

    def test_set_Bit_Number_three(self):
        self.assertEqual(set_Bit_Number(3), 4)

    def test_set_Bit_Number_four(self):
        self.assertEqual(set_Bit_Number(4), 8)

    def test_set_Bit_Number_five(self):
        self.assertEqual(set_Bit_Number(5), 8)

    def test_set_Bit_Number_six(self):
        self.assertEqual(set_Bit_Number(6), 8)

    def test_set_Bit_Number_seven(self):
        self.assertEqual(set_Bit_Number(7), 8)

    def test_set_Bit_Number_eight(self):
        self.assertEqual(set_Bit_Number(8), 8)

    def test_set_Bit_Number_nine(self):
        self.assertEqual(set_Bit_Number(9), 8)

    def test_set_Bit_Number_ten(self):
        self.assertEqual(set_Bit_Number(10), 16)

    def test_set_Bit_Number_negative(self):
        with self.assertRaises(TypeError):
            set_Bit_Number(-1)

    def test_set_Bit_Number_non_integer(self):
        with self.assertRaises(TypeError):
            set_Bit_Number('a')
