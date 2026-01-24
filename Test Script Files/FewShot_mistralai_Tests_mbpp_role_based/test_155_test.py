import unittest
from mbpp_155_code import even_bit_toggle_number

class TestEvenBitToggleNumber(unittest.TestCase):
    def test_even_number(self):
        self.assertEqual(even_bit_toggle_number(4), 6)

    def test_odd_number(self):
        self.assertEqual(even_bit_toggle_number(5), 7)

    def test_zero(self):
        self.assertEqual(even_bit_toggle_number(0), 0)

    def test_negative_number(self):
        self.assertEqual(even_bit_toggle_number(-4), 6)

    def test_max_int(self):
        self.assertEqual(even_bit_toggle_number(2**31 - 1), 2**31 - 1)

    def test_min_int(self):
        self.assertEqual(even_bit_toggle_number(2**31), 2**31 - 1)
