import unittest
from mbpp_958_code import int_to_roman

class TestIntToRoman(unittest.TestCase):

    def test_simple_inputs(self):
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

    def test_edge_conditions(self):
        self.assertEqual(int_to_roman(40), 'XL')
        self.assertEqual(int_to_roman(90), 'XC')
        self.assertEqual(int_to_roman(400), 'CD')
        self.assertEqual(int_to_roman(900), 'CM')
        self.assertEqual(int_to_roman(1000), 'M')

    def test_boundary_conditions(self):
        self.assertEqual(int_to_roman(3999), 'MMMCMXCIX')

    def test_complex_cases(self):
        self.assertEqual(int_to_roman(1994), 'MCMXCIV')
