import unittest
from mbpp_224_code import count_Set_Bits

class TestCountSetBits(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(count_Set_Bits(0), 0)

    def test_single_bit(self):
        self.assertEqual(count_Set_Bits(1), 1)

    def test_multiple_bits(self):
        self.assertEqual(count_Set_Bits(3), 2)

    def test_power_of_two(self):
        self.assertEqual(count_Set_Bits(8), 1)

    def test_max_int(self):
        self.assertEqual(count_Set_Bits(2**31 - 1), 31)

    def test_negative(self):
        with self.assertRaises(TypeError):
            count_Set_Bits(-1)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            count_Set_Bits(3.5)
