import unittest
from mbpp_958_code import int_to_roman

class TestIntToRoman(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(int_to_roman(1), 'I')
        self.assertEqual(int_to_roman(4), 'IV')
        self.assertEqual(int_to_roman(5), 'V')
        self.assertEqual(int_to_roman(6), 'VI')
        self.assertEqual(int_to_roman(10), 'X')
        self.assertEqual(int_to_roman(50), 'L')
        self.assertEqual(int_to_roman(100), 'C')
        self.assertEqual(int_to_roman(500), 'D')
        self.assertEqual(int_to_roman(1000), 'M')
        self.assertEqual(int_to_roman(1999), 'MCMXCIX')

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(int_to_roman(0), '')
        self.assertEqual(int_to_roman(1), 'I')
        self.assertEqual(int_to_roman(3999), 'MMMCMXCIX')

    def test_complex_and_corner_cases(self):
        self.assertEqual(int_to_roman(3), 'III')
        self.assertEqual(int_to_roman(7), 'VII')
        self.assertEqual(int_to_roman(12), 'XII')
        self.assertEqual(int_to_roman(13), 'XIII')
        self.assertEqual(int_to_roman(14), 'XIV')
        self.assertEqual(int_to_roman(15), 'XV')
        self.assertEqual(int_to_roman(16), 'XVI')
        self.assertEqual(int_to_roman(17), 'XVII')
        self.assertEqual(int_to_roman(18), 'XVIII')
        self.assertEqual(int_to_roman(19), 'XIX')
        self.assertEqual(int_to_roman(20), 'XX')
