import unittest
from mbpp_383_code import even_bit_toggle_number

class TestEvenBitToggleNumber(unittest.TestCase):

    def test_even_bit_toggle_normal(self):
        self.assertEqual(even_bit_toggle_number(0), 0)
        self.assertEqual(even_bit_toggle_number(1), 1)
        self.assertEqual(even_bit_toggle_number(2), 3)
        self.assertEqual(even_bit_toggle_number(3), 2)
        self.assertEqual(even_bit_toggle_number(4), 6)
        self.assertEqual(even_bit_toggle_number(5), 7)
        self.assertEqual(even_bit_toggle_number(6), 13)
        self.assertEqual(even_bit_toggle_number(7), 11)
        self.assertEqual(even_bit_toggle_number(8), 15)
        self.assertEqual(even_bit_toggle_number(9), 19)
        self.assertEqual(even_bit_toggle_number(10), 31)
        self.assertEqual(even_bit_toggle_number(11), 33)
        self.assertEqual(even_bit_toggle_number(12), 63)
        self.assertEqual(even_bit_toggle_number(13), 67)
        self.assertEqual(even_bit_toggle_number(14), 127)
        self.assertEqual(even_bit_toggle_number(15), 129)

    def test_edge_cases(self):
        self.assertEqual(even_bit_toggle_number(0x7FFFFFFF), 0x80000000)
        self.assertEqual(even_bit_toggle_number(0x80000000), 0x7FFFFFFF)
        self.assertEqual(even_bit_toggle_number(-1), -3)
        self.assertEqual(even_bit_toggle_number(-2), -5)
        self.assertEqual(even_bit_toggle_number(-3), -7)
        self.assertEqual(even_bit_toggle_number(-4), -9)
        self.assertEqual(even_bit_toggle_number(-5), -11)
        self.assertEqual(even_bit_toggle_number(-6), -13)
        self.assertEqual(even_bit_toggle_number(-7), -15)
        self.assertEqual(even_bit_toggle_number(-8), -17)
        self.assertEqual(even_bit_toggle_number(-9), -19)
        self.assertEqual(even_bit_toggle_number(-10), -21)
        self.assertEqual(even_bit_toggle_number(-11), -23)
        self.assertEqual(even_bit_toggle_number(-12), -25)
        self.assertEqual(even_bit_toggle_number(-13), -27)
        self.assertEqual(even_bit_toggle_number(-14), -29)
        self.assertEqual(even_bit_toggle_number(-15), -31)
        self.assertEqual(even_bit_toggle_number(-0x80000000), 0x7FFFFFFF)
        self.assertEqual(even_bit_toggle_number(-0x7FFFFFFF), 0x80000000)
