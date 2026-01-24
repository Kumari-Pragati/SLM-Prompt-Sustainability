import unittest

from mbpp_155_code import even_bit_toggle_number

class TestEvenBitToggleNumber(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(even_bit_toggle_number(0), 0)
        self.assertEqual(even_bit_toggle_number(1), 2)
        self.assertEqual(even_bit_toggle_number(2), 1)
        self.assertEqual(even_bit_toggle_number(3), 3)
        self.assertEqual(even_bit_toggle_number(4), 5)
        self.assertEqual(even_bit_toggle_number(5), 7)

    def test_edge_cases(self):
        self.assertEqual(even_bit_toggle_number(15), 31)
        self.assertEqual(even_bit_toggle_number(31), 63)
        self.assertEqual(even_bit_toggle_number(63), 127)
        self.assertEqual(even_bit_toggle_number(127), 255)

    def test_corner_cases(self):
        self.assertEqual(even_bit_toggle_number(256), 511)
        self.assertEqual(even_bit_toggle_number(511), 1023)
        self.assertEqual(even_bit_toggle_number(1023), 2047)
        self.assertEqual(even_bit_toggle_number(2047), 4095)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            even_bit_toggle_number("15")
        with self.assertRaises(TypeError):
            even_bit_toggle_number(15.5)
        with self.assertRaises(TypeError):
            even_bit_toggle_number(None)
