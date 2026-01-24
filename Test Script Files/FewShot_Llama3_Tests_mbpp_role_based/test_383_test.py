import unittest
from mbpp_383_code import even_bit_toggle_number

class TestEvenBitToggleNumber(unittest.TestCase):
    def test_even_number(self):
        self.assertEqual(even_bit_toggle_number(10), 10)

    def test_odd_number(self):
        self.assertEqual(even_bit_toggle_number(15), 15)

    def test_zero(self):
        self.assertEqual(even_bit_toggle_number(0), 0)

    def test_negative_number(self):
        self.assertEqual(even_bit_toggle_number(-10), -10)

    def test_large_number(self):
        self.assertEqual(even_bit_toggle_number(1000000), 1000000)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            even_bit_toggle_number("hello")
