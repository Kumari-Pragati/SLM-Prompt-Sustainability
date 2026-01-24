import unittest
from mbpp_958_code import int_to_roman

class TestIntToRoman(unittest.TestCase):

    def test_1_to_I(self):
        self.assertEqual(int_to_roman(1), 'I')

    def test_2_to_II(self):
        self.assertEqual(int_to_roman(2), 'II')

    def test_3_to_III(self):
        self.assertEqual(int_to_roman(3), 'III')

    def test_4_to_IV(self):
        self.assertEqual(int_to_roman(4), 'IV')

    def test_5_to_V(self):
        self.assertEqual(int_to_roman(5), 'V')

    def test_6_to_VI(self):
        self.assertEqual(int_to_roman(6), 'VI')

    def test_7_to_VII(self):
        self.assertEqual(int_to_roman(7), 'VII')

    def test_8_to_VIII(self):
        self.assertEqual(int_to_roman(8), 'VIII')

    def test_9_to_IX(self):
        self.assertEqual(int_to_roman(9), 'IX')

    def test_10_to_X(self):
        self.assertEqual(int_to_roman(10), 'X')

    def test_11_to_XI(self):
        self.assertEqual(int_to_roman(11), 'XI')

    def test_14_to_XIV(self):
        self.assertEqual(int_to_roman(14), 'XIV')

    def test_18_to_XVIII(self):
        self.assertEqual(int_to_roman(18), 'XVIII')

    def test_20_to_XX(self):
        self.assertEqual(int_to_roman(20), 'XX')

    def test_40_to_XL(self):
        self.assertEqual(int_to_roman(40), 'XL')

    def test_50_to_L(self):
        self.assertEqual(int_to_roman(50), 'L')

    def test_90_to_XC(self):
        self.assertEqual(int_to_roman(90), 'XC')

    def test_100_to_C(self):
        self.assertEqual(int_to_roman(100), 'C')

    def test_400_to_CD(self):
        self.assertEqual(int_to_roman(400), 'CD')

    def test_500_to_D(self):
        self.assertEqual(int_to_roman(500), 'D')

    def test_900_to_CM(self):
        self.assertEqual(int_to_roman(900), 'CM')

    def test_1000_to_M(self):
        self.assertEqual(int_to_roman(1000), 'M')

    def test_1984_to_MCMLXXXIV(self):
        self.assertEqual(int_to_roman(1984), 'MCMLXXXIV')

    def test_3999_to_MMMCMXCIX(self):
        self.assertEqual(int_to_roman(3999), 'MMMCMXCIX')
