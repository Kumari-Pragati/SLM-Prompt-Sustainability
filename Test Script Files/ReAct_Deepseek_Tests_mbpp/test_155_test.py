import unittest
from mbpp_155_code import even_bit_toggle_number

class TestEvenBitToggleNumber(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(even_bit_toggle_number(0), 0)
        self.assertEqual(even_bit_toggle_number(1), 2)
        self.assertEqual(even_bit_toggle_number(2), 1)
        self.assertEqual(even_bit_toggle_number(3), 3)
        self.assertEqual(even_bit_toggle_number(4), 5)
        self.assertEqual(even_bit_toggle_number(5), 4)
        self.assertEqual(even_bit_toggle_number(6), 7)
        self.assertEqual(even_bit_toggle_number(7), 6)
        self.assertEqual(even_bit_toggle_number(8), 9)

    def test_edge_cases(self):
        self.assertEqual(even_bit_toggle_number(0xFFFFFFFF), 0xFFFFFFFE)
        self.assertEqual(even_bit_toggle_number(0x80000000), 0x7FFFFFFF)

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            even_bit_toggle_number("invalid")
        with self.assertRaises(ValueError):
            even_bit_toggle_number(-1)
