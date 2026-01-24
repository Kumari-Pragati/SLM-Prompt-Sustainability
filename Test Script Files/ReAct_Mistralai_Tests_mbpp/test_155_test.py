import unittest
from mbpp_155_code import even_bit_toggle_number

class TestEvenBitToggleNumber(unittest.TestCase):

    def test_even_bit_toggle_normal(self):
        self.assertEqual(even_bit_toggle_number(0), 0)
        self.assertEqual(even_bit_toggle_number(1), 1)
        self.assertEqual(even_bit_toggle_number(2), 3)
        self.assertEqual(even_bit_toggle_number(3), 2)
        self.assertEqual(even_bit_toggle_number(4), 6)
        self.assertEqual(even_bit_toggle_number(5), 7)

    def test_edge_cases(self):
        self.assertEqual(even_bit_toggle_number(0x7FFFFFFF), 0x80000000)
        self.assertEqual(even_bit_toggle_number(0x80000000), 0x7FFFFFFF)
        self.assertEqual(even_bit_toggle_number(-1), -3)
        self.assertEqual(even_bit_toggle_number(-2), -3)

    def test_error_handling(self):
        self.assertRaises(TypeError, even_bit_toggle_number, 'not_a_number')
