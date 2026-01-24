import unittest
from mbpp_78_code import count_With_Odd_SetBits

class TestCountWithOddSetBits(unittest.TestCase):

    def test_count_with_odd_set_bits_positive(self):
        self.assertEqual(count_With_Odd_SetBits(1), 0.5)
        self.assertEqual(count_With_Odd_SetBits(3), 1.5)
        self.assertEqual(count_With_Odd_SetBits(5), 2.5)
        self.assertEqual(count_With_Odd_SetBits(7), 3.5)
        self.assertEqual(count_With_Odd_SetBits(9), 4.5)

    def test_count_with_odd_set_bits_zero(self):
        self.assertEqual(count_With_Odd_SetBits(0), 0.0)

    def test_count_with_odd_set_bits_negative(self):
        self.assertEqual(count_With_Odd_SetBits(-1), 0.0)
        self.assertEqual(count_With_Odd_SetBits(-3), -1.0)
        self.assertEqual(count_With_Odd_SetBits(-5), -2.0)
        self.assertEqual(count_With_Odd_SetBits(-7), -3.0)
        self.assertEqual(count_With_Odd_SetBits(-9), -4.0)
