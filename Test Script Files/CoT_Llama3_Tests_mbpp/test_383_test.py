import unittest
from mbpp_383_code import even_bit_toggle_number

class TestEvenBitToggleNumber(unittest.TestCase):
    def test_even_bit_toggle_number_positive(self):
        self.assertEqual(even_bit_toggle_number(10), 10)
        self.assertEqual(even_bit_toggle_number(15), 15)
        self.assertEqual(even_bit_toggle_number(20), 20)

    def test_even_bit_toggle_number_negative(self):
        self.assertEqual(even_bit_toggle_number(-10), -10)
        self.assertEqual(even_bit_toggle_number(-15), -15)
        self.assertEqual(even_bit_toggle_number(-20), -20)

    def test_even_bit_toggle_number_zero(self):
        self.assertEqual(even_bit_toggle_number(0), 0)

    def test_even_bit_toggle_number_large(self):
        self.assertEqual(even_bit_toggle_number(1000000), 1000000)
        self.assertEqual(even_bit_toggle_number(-1000000), -1000000)

    def test_even_bit_toggle_number_edge(self):
        self.assertEqual(even_bit_toggle_number(1), 1)
        self.assertEqual(even_bit_toggle_number(-1), -1)
