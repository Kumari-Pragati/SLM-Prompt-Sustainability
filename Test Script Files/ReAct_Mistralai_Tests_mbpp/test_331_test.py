import unittest
from mbpp_331_code import count_unset_bits

class TestCountUnsetBits(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(count_unset_bits(0), 1)

    def test_single_bit(self):
        for bit in range(1, 32):
            self.assertEqual(count_unset_bits(1 << bit), bit)

    def test_multiple_bits(self):
        for num in range(1, 32):
            for bit in range(1, num + 1):
                test_num = (1 << bit) | num
                self.assertEqual(count_unset_bits(test_num), num)

    def test_negative_number(self):
        self.assertRaises(ValueError, count_unset_bits, -1)

    def test_large_number(self):
        self.assertRaises(OverflowError, count_unset_bits, (1 << 31))
