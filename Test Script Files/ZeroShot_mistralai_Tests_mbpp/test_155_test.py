import unittest
from mbpp_155_code import even_bit_toggle_number

class TestEvenBitToggleNumber(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(even_bit_toggle_number(0), 0)

    def test_one(self):
        self.assertEqual(even_bit_toggle_number(1), 1)

    def test_even_number(self):
        self.assertEqual(even_bit_toggle_number(2), 2)
        self.assertEqual(even_bit_toggle_number(4), 6)
        self.assertEqual(even_bit_toggle_number(10), 14)

    def test_odd_number(self):
        self.assertEqual(even_bit_toggle_number(3), 4)
        self.assertEqual(even_bit_toggle_number(5), 6)
        self.assertEqual(even_bit_toggle_number(15), 18)
