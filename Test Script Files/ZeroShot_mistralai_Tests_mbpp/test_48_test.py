import unittest
from mbpp_48_code import odd_bit_set_number

class TestOddBitSetNumber(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(odd_bit_set_number(0), 0)

    def test_one(self):
        self.assertEqual(odd_bit_set_number(1), 1)

    def test_powers_of_two(self):
        for i in range(1, 32):
            self.assertEqual(odd_bit_set_number(2 ** i), 2 ** i)

    def test_negative_numbers(self):
        for i in range(-10, 0):
            self.assertEqual(odd_bit_set_number(i), odd_bit_set_number(-i))

    def test_bitwise_operations(self):
        self.assertEqual(odd_bit_set_number(0b1010), 0b1110)
        self.assertEqual(odd_bit_set_number(0o12), 0o20)
        self.assertEqual(odd_bit_set_number(0xCAFE), 0xFDFE)
