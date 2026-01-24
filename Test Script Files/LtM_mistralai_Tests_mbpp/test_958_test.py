import unittest
from mbpp_958_code import int_to_roman

class TestIntToRoman(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(int_to_roman(1), 'I')
        self.assertEqual(int_to_roman(3), 'III')
        self.assertEqual(int_to_roman(4), 'IV')
        self.assertEqual(int_to_roman(9), 'IX')
        self.assertEqual(int_to_roman(58), 'LVIII')
        self.assertEqual(int_to_roman(499), 'CDXCIX')

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(int_to_roman(0), '')
        self.assertEqual(int_to_roman(1000), 'M')
        self.assertEqual(int_to_roman(3999), 'MMMCMXCIX')
        self.assertEqual(int_to_roman(4000), 'Error: Input value exceeds the maximum supported range')

    def test_complex_inputs(self):
        self.assertEqual(int_to_roman(2018), 'MMXVIII')
        self.assertEqual(int_to_roman(3000), 'MMM')
        self.assertEqual(int_to_roman(4001), 'Error: Input value exceeds the maximum supported range')
