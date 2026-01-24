import unittest
from mbpp_383_code import even_bit_toggle_number

class TestEvenBitToggleNumber(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(even_bit_toggle_number(1), 1)
        self.assertEqual(even_bit_toggle_number(2), 2)
        self.assertEqual(even_bit_toggle_number(3), 1)
        self.assertEqual(even_bit_toggle_number(4), 4)
        self.assertEqual(even_bit_toggle_number(5), 1)
        self.assertEqual(even_bit_toggle_number(6), 6)
        self.assertEqual(even_bit_toggle_number(7), 1)
        self.assertEqual(even_bit_toggle_number(8), 8)

    def test_edge(self):
        self.assertEqual(even_bit_toggle_number(0), 0)
        self.assertEqual(even_bit_toggle_number(9), 9)
        self.assertEqual(even_bit_toggle_number(10), 10)
        self.assertEqual(even_bit_toggle_number(11), 11)
        self.assertEqual(even_bit_toggle_number(12), 12)
        self.assertEqual(even_bit_toggle_number(13), 13)
        self.assertEqual(even_bit_toggle_number(14), 14)
        self.assertEqual(even_bit_toggle_number(15), 15)

    def test_complex(self):
        self.assertEqual(even_bit_toggle_number(16), 16)
        self.assertEqual(even_bit_toggle_number(17), 17)
        self.assertEqual(even_bit_toggle_number(18), 18)
        self.assertEqual(even_bit_toggle_number(19), 19)
        self.assertEqual(even_bit_toggle_number(20), 20)
        self.assertEqual(even_bit_toggle_number(21), 21)
        self.assertEqual(even_bit_toggle_number(22), 22)
        self.assertEqual(even_bit_toggle_number(23), 23)
        self.assertEqual(even_bit_toggle_number(24), 24)
