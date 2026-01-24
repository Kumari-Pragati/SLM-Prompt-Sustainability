import unittest
from mbpp_383_code import even_bit_toggle_number

class TestEvenBitToggleNumber(unittest.TestCase):
    def test_even_bit_toggle_positive_number(self):
        self.assertEqual(even_bit_toggle_number(4), 6)
        self.assertEqual(even_bit_toggle_number(6), 2)

    def test_odd_bit_toggle_positive_number(self):
        self.assertEqual(even_bit_toggle_number(5), 7)
        self.assertEqual(even_bit_toggle_number(7), 3)

    def test_zero(self):
        self.assertEqual(even_bit_toggle_number(0), 1)

    def test_negative_number(self):
        self.assertEqual(even_bit_toggle_number(-4), 6)
        self.assertEqual(even_bit_toggle_number(-6), 2)

    def test_bitwise_not_with_itself(self):
        self.assertEqual(even_bit_toggle_number(1), 1)
        self.assertEqual(even_bit_toggle_number(2), 3)
        self.assertEqual(even_bit_toggle_number(3), 7)
        self.assertEqual(even_bit_toggle_number(4), 6)
        self.assertEqual(even_bit_toggle_number(5), 7)
        self.assertEqual(even_bit_toggle_number(6), 2)
        self.assertEqual(even_bit_toggle_number(7), 3)
