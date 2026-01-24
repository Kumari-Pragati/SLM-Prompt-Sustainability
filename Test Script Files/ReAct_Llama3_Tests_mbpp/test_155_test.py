import unittest
from mbpp_155_code import even_bit_toggle_number

class TestEvenBitToggleNumber(unittest.TestCase):

    def test_even_number(self):
        self.assertEqual(even_bit_toggle_number(10), 10)

    def test_odd_number(self):
        self.assertEqual(even_bit_toggle_number(11), 11)

    def test_single_bit_toggle(self):
        self.assertEqual(even_bit_toggle_number(15), 15)

    def test_multiple_bit_toggle(self):
        self.assertEqual(even_bit_toggle_number(24), 24)

    def test_zero_input(self):
        self.assertEqual(even_bit_toggle_number(0), 0)

    def test_negative_input(self):
        self.assertEqual(even_bit_toggle_number(-10), -10)

    def test_large_number(self):
        self.assertEqual(even_bit_toggle_number(1000000), 1000000)
