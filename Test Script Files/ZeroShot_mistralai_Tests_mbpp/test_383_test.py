import unittest
from mbpp_383_code import even_bit_toggle_number

class TestEvenBitToggleNumber(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(even_bit_toggle_number(0), 0)

    def test_one(self):
        self.assertEqual(even_bit_toggle_number(1), 2)

    def test_even_number(self):
        self.assertEqual(even_bit_toggle_number(4), 6)

    def test_odd_number(self):
        self.assertEqual(even_bit_toggle_number(5), 10)

    def test_negative_number(self):
        self.assertEqual(even_bit_toggle_number(-3), 14)
