import unittest
from mbpp_155_code import even_bit_toggle_number

class TestEvenBitToggleNumber(unittest.TestCase):
    def test_even_bit_toggle_number_typical(self):
        self.assertEqual(even_bit_toggle_number(10), 10)
        self.assertEqual(even_bit_toggle_number(15), 15)
        self.assertEqual(even_bit_toggle_number(20), 20)

    def test_even_bit_toggle_number_edge(self):
        self.assertEqual(even_bit_toggle_number(0), 0)
        self.assertEqual(even_bit_toggle_number(1), 1)
        self.assertEqual(even_bit_toggle_number(2), 2)

    def test_even_bit_toggle_number_corner(self):
        self.assertEqual(even_bit_toggle_number(3), 1)
        self.assertEqual(even_bit_toggle_number(4), 4)
        self.assertEqual(even_bit_toggle_number(5), 1)

    def test_even_bit_toggle_number_invalid(self):
        with self.assertRaises(TypeError):
            even_bit_toggle_number('a')
