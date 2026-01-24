import unittest
from mbpp_903_code import count_Unset_Bits

class TestCountUnsetBits(unittest.TestCase):

    def test_zero_input(self):
        self.assertEqual(count_Unset_Bits(0), 0)

    def test_single_bit_set(self):
        self.assertEqual(count_Unset_Bits(1), 0)

    def test_single_bit_unset(self):
        self.assertEqual(count_Unset_Bits(2), 1)

    def test_multiple_bits_unset(self):
        self.assertEqual(count_Unset_Bits(3), 2)

    def test_multiple_bits_set(self):
        self.assertEqual(count_Unset_Bits(4), 2)

    def test_large_number(self):
        self.assertEqual(count_Unset_Bits(1024), 10)

    def test_negative_number(self):
        with self.assertRaises(TypeError):
            count_Unset_Bits(-1)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            count_Unset_Bits('a')
