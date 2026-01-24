import unittest
from mbpp_958_code import int_to_roman

class TestIntToRoman(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(int_to_roman(1), 'I')
        self.assertEqual(int_to_roman(3), 'III')
        self.assertEqual(int_to_roman(4), 'IV')
        self.assertEqual(int_to_roman(5), 'V')
        self.assertEqual(int_to_roman(9), 'IX')
        self.assertEqual(int_to_roman(10), 'X')
        self.assertEqual(int_to_roman(40), 'XL')
        self.assertEqual(int_to_roman(50), 'L')
        self.assertEqual(int_to_roman(90), 'XC')
        self.assertEqual(int_to_roman(100), 'C')
        self.assertEqual(int_to_roman(400), 'CD')
        self.assertEqual(int_to_roman(500), 'D')
        self.assertEqual(int_to_roman(900), 'CM')
        self.assertEqual(int_to_roman(1000), 'M')
        self.assertEqual(int_to_roman(2000), 'MM')
        self.assertEqual(int_to_roman(3000), 'MMM')

    def test_edge_and_boundary_cases(self):
        self.assertEqual(int_to_roman(0), '')
        self.assertEqual(int_to_roman(2), 'II')
        self.assertEqual(int_to_roman(6), 'VI')
        self.assertEqual(int_to_roman(8), 'VIII')
        self.assertEqual(int_to_roman(19), 'XIX')
        self.assertEqual(int_to_roman(49), 'XLIX')
        self.assertEqual(int_to_roman(99), 'XCIX')
        self.assertEqual(int_to_roman(499), 'CDXCIX')
        self.assertEqual(int_to_roman(999), 'CMXCIX')
        self.assertEqual(int_to_roman(2000000), 'MMD')
