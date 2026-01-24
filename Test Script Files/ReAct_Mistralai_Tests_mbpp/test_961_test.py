import unittest
from mbpp_961_code import roman_to_int

class TestRomanToInt(unittest.TestCase):

    def test_simple_roman_numbers(self):
        self.assertEqual(roman_to_int('I'), 1)
        self.assertEqual(roman_to_int('IV'), 4)
        self.assertEqual(roman_to_int('IX'), 9)
        self.assertEqual(roman_to_int('X'), 10)
        self.assertEqual(roman_to_int('XL'), 40)
        self.assertEqual(roman_to_int('XC'), 90)
        self.assertEqual(roman_to_int('C'), 100)
        self.assertEqual(roman_to_int('CD'), 400)
        self.assertEqual(roman_to_int('CM'), 900)
        self.assertEqual(roman_to_int('M'), 1000)

    def test_mixed_roman_numbers(self):
        self.assertEqual(roman_to_int('III'), 3)
        self.assertEqual(roman_to_int('VIII'), 8)
        self.assertEqual(roman_to_int('XIII'), 13)
        self.assertEqual(roman_to_int('XVIII'), 18)
        self.assertEqual(roman_to_int('XXIII'), 23)
        self.assertEqual(roman_to_int('XXVIII'), 28)
        self.assertEqual(roman_to_int('XXXIII'), 33)
        self.assertEqual(roman_to_int('LIII'), 53)
        self.assertEqual(roman_to_int('LVIII'), 58)
        self.assertEqual(roman_to_int('LXXXIII'), 83)
        self.assertEqual(roman_to_int('DIII'), 303)
        self.assertEqual(roman_to_int('DIV'), 504)
        self.assertEqual(roman_to_int('DVIII'), 508)
        self.assertEqual(roman_to_int('DXIII'), 513)
        self.assertEqual(roman_to_int('DXVIII'), 518)
        self.assertEqual(roman_to_int('DXXIII'), 523)
        self.assertEqual(roman_to_int('DXXVIII'), 528)
        self.assertEqual(roman_to_int('DXXXIII'), 533)
        self.assertEqual(roman_to_int('LIV'), 54)
        self.assertEqual(roman_to_int('LV'), 55)
        self.assertEqual(roman_to_int('LXV'), 65)
        self.assertEqual(roman_to_int('LXXV'), 75)
        self.assertEqual(roman_to_int('LXXXV'), 85)
        self.assertEqual(roman_to_int('XLIV'), 44)
        self.assertEqual(roman_to_int('XLV'), 45)
        self.assertEqual(roman_to_int('XLXIV'), 49)
        self.assertEqual(roman_to_int('XLXV'), 49)
        self.assertEqual(roman_to_int('XLXXIV'), 54)
        self.assertEqual(roman_to_int('XLXXV'), 55)
        self.assertEqual(roman_to_int('XLXXXIV'), 59)
        self.assertEqual(roman_to_int('XLXXXV'), 59)

    def test_empty_string(self):
        self.assertEqual(roman_to_int(''), 0)

    def test_invalid_roman_numbers(self):
        self.assertRaises(ValueError, roman_to_int, 'A')
        self.assertRaises(ValueError, roman_to_int, 'IVV')
        self.assertRaises(ValueError, roman_to_int,