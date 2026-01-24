import unittest
from mbpp_958_code import int_to_roman

class TestIntToRoman(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(int_to_roman(1), 'I')
        self.assertEqual(int_to_roman(4), 'IV')
        self.assertEqual(int_to_roman(6), 'VI')
        self.assertEqual(int_to_roman(10), 'X')
        self.assertEqual(int_to_roman(50), 'L')
        self.assertEqual(int_to_roman(100), 'C')
        self.assertEqual(int_to_roman(500), 'D')
        self.assertEqual(int_to_roman(1000), 'M')

    def test_edge_cases(self):
        self.assertEqual(int_to_roman(40), 'XL')
        self.assertEqual(int_to_roman(90), 'XC')
        self.assertEqual(int_to_roman(400), 'CD')
        self.assertEqual(int_to_roman(900), 'CM')

    def test_corner_cases(self):
        self.assertEqual(int_to_roman(3999), 'MMMCMXCIX')
        self.assertEqual(int_to_roman(2019), 'MMXIX')

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            int_to_roman('a')
        with self.assertRaises(ValueError):
            int_to_roman(-1)
        with self.assertRaises(ValueError):
            int_to_roman(4000)
