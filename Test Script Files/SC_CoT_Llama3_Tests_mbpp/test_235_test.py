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

    def test_even_bit_set_number_one(self):
        self.assertEqual(even_bit_set_number(1), 1)

    def test_even_bit_set_number_large(self):
        self.assertEqual(even_bit_set_number(1000), 1022)
        self.assertEqual(even_bit_set_number(1001), 1023)

    def test_even_bit_set_number_invalid_input(self):
        with self.assertRaises(TypeError):
            even_bit_set_number('a')
