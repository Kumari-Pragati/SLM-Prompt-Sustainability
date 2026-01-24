import unittest
from mbpp_467_code import decimal_to_Octal

class TestDecimalToOctal(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(decimal_to_Octal(0), '0')

    def test_one(self):
        self.assertEqual(decimal_to_Octal(1), '1')

    def test_two(self):
        self.assertEqual(decimal_to_Octal(2), '2')

    def test_three(self):
        self.assertEqual(decimal_to_Octal(3), '3')

    def test_four(self):
        self.assertEqual(decimal_to_Octal(4), '4')

    def test_five(self):
        self.assertEqual(decimal_to_Octal(5), '5')

    def test_six(self):
        self.assertEqual(decimal_to_Octal(6), '6')

    def test_seven(self):
        self.assertEqual(decimal_to_Octal(7), '7')

    def test_eight(self):
        self.assertEqual(decimal_to_Octal(8), '10')

    def test_nine(self):
        self.assertEqual(decimal_to_Octal(9), '11')

    def test_ten(self):
        self.assertEqual(decimal_to_Octal(10), '12')

    def test_twenty(self):
        self.assertEqual(decimal_to_Octal(20), '22')

    def test_hundred(self):
        self.assertEqual(decimal_to_Octal(100), '141')

    def test_thousand(self):
        self.assertEqual(decimal_to_Octal(1000), '1000')

    def test_negative_number(self):
        self.assertEqual(decimal_to_Octal(-1), '377')

    def test_large_number(self):
        self.assertEqual(decimal_to_Octal(123456789), '20111111111')
