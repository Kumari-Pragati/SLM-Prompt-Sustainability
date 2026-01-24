import unittest
from mbpp_155_code import even_bit_toggle_number

class TestEvenBitToggleNumber(unittest.TestCase):

    def test_even_bit_toggle_number(self):
        self.assertEqual(even_bit_toggle_number(0), 0)
        self.assertEqual(even_bit_toggle_number(1), 2)
        self.assertEqual(even_bit_toggle_number(2), 1)
        self.assertEqual(even_bit_toggle_number(3), 3)
        self.assertEqual(even_bit_toggle_number(4), 5)
        self.assertEqual(even_bit_toggle_number(5), 7)
        self.assertEqual(even_bit_toggle_number(6), 3)
        self.assertEqual(even_bit_toggle_number(7), 7)
        self.assertEqual(even_bit_toggle_number(8), 9)
        self.assertEqual(even_bit_toggle_number(9), 11)
        self.assertEqual(even_bit_toggle_number(10), 5)
        self.assertEqual(even_bit_toggle_number(11), 11)
        self.assertEqual(even_bit_toggle_number(12), 13)
        self.assertEqual(even_bit_toggle_number(13), 15)
        self.assertEqual(even_bit_toggle_number(14), 7)
        self.assertEqual(even_bit_toggle_number(15), 15)
