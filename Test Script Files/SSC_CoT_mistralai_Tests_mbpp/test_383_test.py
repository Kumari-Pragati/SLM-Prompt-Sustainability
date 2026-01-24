import unittest
from mbpp_383_code import even_bit_toggle_number

class TestEvenBitToggleNumber(unittest.TestCase):
    def test_even_bit_toggle_normal(self):
        self.assertEqual(even_bit_toggle_number(10), 18)
        self.assertEqual(even_bit_toggle_number(20), 22)
        self.assertEqual(even_bit_toggle_number(255), 253)
        self.assertEqual(even_bit_toggle_number(16777215), 16777213)

    def test_even_bit_toggle_edge_cases(self):
        self.assertEqual(even_bit_toggle_number(0), 0)
        self.assertEqual(even_bit_toggle_number(1), 1)
        self.assertEqual(even_bit_toggle_number(2), 3)
        self.assertEqual(even_bit_toggle_number(3), 7)
        self.assertEqual(even_bit_toggle_number(4), 6)
        self.assertEqual(even_bit_toggle_number(5), 7)

    def test_even_bit_toggle_special_cases(self):
        self.assertEqual(even_bit_toggle_number(12), 13)
        self.assertEqual(even_bit_toggle_number(14), 15)
        self.assertEqual(even_bit_toggle_number(1331), 1333)
        self.assertEqual(even_bit_toggle_number(2147483647), 2147483645)
