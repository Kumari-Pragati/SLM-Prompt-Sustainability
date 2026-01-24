import unittest
from mbpp_383_code import even_bit_toggle_number

class TestEvenBitToggleNumber(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(even_bit_toggle_number(0), 0)
        self.assertEqual(even_bit_toggle_number(1), 2)
        self.assertEqual(even_bit_toggle_number(2), 1)
        self.assertEqual(even_bit_toggle_number(3), 3)
        self.assertEqual(even_bit_toggle_number(4), 5)
        self.assertEqual(even_bit_toggle_number(5), 7)
        self.assertEqual(even_bit_toggle_number(6), 6)
        self.assertEqual(even_bit_toggle_number(7), 7)

    def test_edge_cases(self):
        self.assertEqual(even_bit_toggle_number(8), 10)
        self.assertEqual(even_bit_toggle_number(9), 11)
        self.assertEqual(even_bit_toggle_number(10), 12)
        self.assertEqual(even_bit_toggle_number(11), 13)
        self.assertEqual(even_bit_toggle_number(12), 14)
        self.assertEqual(even_bit_toggle_number(13), 15)
        self.assertEqual(even_bit_toggle_number(14), 14)
        self.assertEqual(even_bit_toggle_number(15), 15)

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            even_bit_toggle_number('a')
        with self.assertRaises(TypeError):
            even_bit_toggle_number(None)
        with self.assertRaises(TypeError):
            even_bit_toggle_number([])
