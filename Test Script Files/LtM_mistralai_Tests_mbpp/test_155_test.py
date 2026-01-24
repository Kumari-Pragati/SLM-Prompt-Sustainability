import unittest
from mbpp_155_code import even_bit_toggle_number

class TestEvenBitToggleNumber(unittest.TestCase):

    def test_simple_even(self):
        self.assertEqual(even_bit_toggle_number(4), 6)
        self.assertEqual(even_bit_toggle_number(14), 18)

    def test_simple_odd(self):
        self.assertEqual(even_bit_toggle_number(3), 5)
        self.assertEqual(even_bit_toggle_number(15), 17)

    def test_edge_min(self):
        self.assertEqual(even_bit_toggle_number(0), 0)

    def test_edge_max(self):
        self.assertEqual(even_bit_toggle_number(2**31 - 1), 2**31 - 1)

    def test_edge_negative(self):
        self.assertEqual(even_bit_toggle_number(-1), 2**31 - 1)
        self.assertEqual(even_bit_toggle_number(-2**31), 0)
