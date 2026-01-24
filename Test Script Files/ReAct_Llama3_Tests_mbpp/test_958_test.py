import unittest
from mbpp_958_code import int_to_roman

class TestIntToRoman(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(int_to_roman(0), '')

    def test_single_digit(self):
        self.assertEqual(int_to_roman(1), 'I')
        self.assertEqual(int_to_roman(2), 'II')
        self.assertEqual(int_to_roman(3), 'III')
        self.assertEqual(int_to_roman(4), 'IV')
        self.assertEqual(int_to_roman(5), 'V')
        self.assertEqual(int_to_roman(6), 'VI')
        self.assertEqual(int_to_roman(7), 'VII')
        self.assertEqual(int_to_roman(8), 'VIII')
        self.assertEqual(int_to_roman(9), 'IX')
        self.assertEqual(int_to_roman(10), 'X')

    def test_tens(self):
        self.assertEqual(int_to_roman(11), 'XI')
        self.assertEqual(int_to_roman(12), 'XII')
        self.assertEqual(int_to_roman(13), 'XIII')
        self.assertEqual(int_to_roman(14), 'XIV')
        self.assertEqual(int_to_roman(15), 'XV')
        self.assertEqual(int_to_roman(16), 'XVI')
        self.assertEqual(int_to_roman(17), 'XVII')
        self.assertEqual(int_to_roman(18), 'XVIII')
        self.assertEqual(int_to_roman(19), 'XIX')
        self.assertEqual(int_to_roman(20), 'XX')

    def test_hundreds(self):
        self.assertEqual(int_to_roman(21), 'XXI')
        self.assertEqual(int_to_roman(22), 'XXII')
        self.assertEqual(int_to_roman(23), 'XXIII')
        self.assertEqual(int_to_roman(24), 'XXIV')
        self.assertEqual(int_to_roman(25), 'XXV')
        self.assertEqual(int_to_roman(26), 'XXVI')
        self.assertEqual(int_to_roman(27), 'XXVII')
        self.assertEqual(int_to_roman(28), 'XXVIII')
        self.assertEqual(int_to_roman(29), 'XXIX')
        self.assertEqual(int_to_roman(30), 'XXX')

    def test_thousands(self):
        self.assertEqual(int_to_roman(31), 'XXXI')
        self.assertEqual(int_to_roman(32), 'XXXII')
        self.assertEqual(int_to_roman(33), 'XXXIII')
        self.assertEqual(int_to_roman(34), 'XXXIV')
        self.assertEqual(int_to_roman(35), 'XXXV')
        self.assertEqual(int_to_roman(36), 'XXXVI')
        self.assertEqual(int_to_roman(37), 'XXXVII')
        self.assertEqual(int_to_roman(38), 'XXXVIII')
        self.assertEqual(int_to_roman(39), 'XXXIX')
        self.assertEqual(int_to_roman(40), 'XL')

    def test_large_numbers(self):
        self.assertEqual(int_to_roman(41), 'XLI')
        self.assertEqual(int_to_roman(42), 'XLII')
        self.assertEqual(int_to_roman(43), 'XLIII')
        self.assertEqual(int_to_roman(44), 'XLIV')
        self.assertEqual(int_to_roman(45), 'XLV')
        self.assertEqual(int_to_roman(46), 'XLVI')
        self.assertEqual(int_to_roman(47), 'XLVII')
        self.assertEqual(int_to_roman(48), 'XLVIII')
        self.assertEqual(int_to_roman(49), 'XLIX')
        self.assertEqual(int_to_roman(50), 'L')

    def test_large_numbers_2(self):
        self.assertEqual(int_to_roman(51), 'LI')
        self.assertEqual(int_to_roman(52), 'LII')
        self.assertEqual(int_to_roman(53), 'LIII')
        self.assertEqual(int_to_roman(54), 'LIV')
        self.assertEqual(int_to_roman(55), 'LV')
        self.assertEqual(int_to_roman(56), 'LVI')
        self.assertEqual(int_to_roman(57), 'LVII')
        self.assertEqual(int_to_roman(58), 'LVIII')
        self.assertEqual(int_to_roman(59), 'LIX')
        self.assertEqual(int_to_roman(60), 'LX')

    def test_large_numbers_3(self):
        self.assertEqual(int_to_roman(61), 'LXI')
        self.assertEqual(int_to_roman(62), 'LXII')
        self.assertEqual(int_to_roman(63), 'LXIII')
        self.assertEqual(int_to_roman(64), 'LXIV')
        self.assertEqual(int_to_roman(65), 'LXV')
        self.assertEqual(int_to_roman(66), 'LXVI')
        self.assertEqual(int_to_roman(