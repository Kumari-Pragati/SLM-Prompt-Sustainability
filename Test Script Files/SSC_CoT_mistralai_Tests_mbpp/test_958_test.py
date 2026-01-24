import unittest
from mbpp_958_code import int_to_roman

class TestIntToRoman(unittest.TestCase):

    def test_normal_inputs(self):
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
        self.assertEqual(int_to_roman(14), 'XIV')
        self.assertEqual(int_to_roman(49), 'XLIX')
        self.assertEqual(int_to_roman(99), 'XCIX')
        self.assertEqual(int_to_roman(400), 'CD')
        self.assertEqual(int_to_roman(500), 'D')
        self.assertEqual(int_to_roman(900), 'CM')
        self.assertEqual(int_to_roman(1000), 'M')

    def test_edge_cases(self):
        self.assertEqual(int_to_roman(0), '')
        self.assertEqual(int_to_roman(2000), 'MMM')
        self.assertEqual(int_to_roman(3000), 'MMM')
        self.assertEqual(int_to_roman(4000), 'MMM')

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, int_to_roman, -1)
        self.assertRaises(ValueError, int_to_roman, float('inf'))
        self.assertRaises(ValueError, int_to_roman, float('-inf'))
