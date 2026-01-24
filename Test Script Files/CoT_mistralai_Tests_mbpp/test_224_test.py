import unittest
from mbpp_224_code import count_Set_Bits

class TestCountSetBits(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(count_Set_Bits(0), 0)

    def test_one(self):
        self.assertEqual(count_Set_Bits(1), 1)

    def test_powers_of_two(self):
        for i in range(1, 16):
            self.assertEqual(count_Set_Bits(2**i), i)

    def test_negative_numbers(self):
        self.assertEqual(count_Set_Bits(-1), 1)
        self.assertEqual(count_Set_Bits(-2), 1)
        self.assertEqual(count_Set_Bits(-3), 2)

    def test_large_positive_numbers(self):
        self.assertEqual(count_Set_Bits(2**31 - 1), 31)
        self.assertEqual(count_Set_Bits(2**63 - 1), 63)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, count_Set_Bits, 'a')
        self.assertRaises(TypeError, count_Set_Bits, 2.5)
        self.assertRaises(TypeError, count_Set_Bits, [1, 2, 3])
