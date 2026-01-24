import unittest
from mbpp_331_code import count_unset_bits

class TestCountUnsetBits(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(count_unset_bits(0), 1)

    def test_one(self):
        self.assertEqual(count_unset_bits(1), 1)

    def test_powers_of_two(self):
        for i in range(1, 16):
            self.assertEqual(count_unset_bits(2**i), i)

    def test_negative_numbers(self):
        self.assertEqual(count_unset_bits(-1), 31)
        self.assertEqual(count_unset_bits(-2), 30)
        self.assertEqual(count_unset_bits(-3), 29)

    def test_large_positive_numbers(self):
        self.assertEqual(count_unset_bits(2**31 - 1), 31)
        self.assertEqual(count_unset_bits(2**32 - 1), 0)

    def test_invalid_input(self):
        self.assertRaises(TypeError, count_unset_bits, 'invalid')
        self.assertRaises(TypeError, count_unset_bits, 2.5)
        self.assertRaises(TypeError, count_unset_bits, [1, 2, 3])
