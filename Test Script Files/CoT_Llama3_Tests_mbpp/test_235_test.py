import unittest
from mbpp_235_code import even_bit_set_number

class TestEvenBitSetNumber(unittest.TestCase):
    def test_even_bit_set_number_positive(self):
        self.assertEqual(even_bit_set_number(10), 14)
        self.assertEqual(even_bit_set_number(15), 15)
        self.assertEqual(even_bit_set_number(20), 22)
        self.assertEqual(even_bit_set_number(25), 25)

    def test_even_bit_set_number_negative(self):
        self.assertEqual(even_bit_set_number(-10), -14)
        self.assertEqual(even_bit_set_number(-15), -15)
        self.assertEqual(even_bit_set_number(-20), -22)
        self.assertEqual(even_bit_set_number(-25), -25)

    def test_even_bit_set_number_zero(self):
        self.assertEqual(even_bit_set_number(0), 0)

    def test_even_bit_set_number_edge(self):
        self.assertEqual(even_bit_set_number(1), 1)
        self.assertEqual(even_bit_set_number(2), 2)
        self.assertEqual(even_bit_set_number(3), 3)
        self.assertEqual(even_bit_set_number(4), 4)

    def test_even_bit_set_number_invalid(self):
        with self.assertRaises(TypeError):
            even_bit_set_number("a")
        with self.assertRaises(TypeError):
            even_bit_set_number(None)
