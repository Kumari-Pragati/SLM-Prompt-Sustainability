import unittest
from mbpp_78_code import count_With_Odd_SetBits

class TestCountWithOddSetBits(unittest.TestCase):

    def test_odd_number(self):
        self.assertEqual(count_With_Odd_SetBits(7), 4)

    def test_even_number_with_odd_set_bits(self):
        self.assertEqual(count_With_Odd_SetBits(10), 5)

    def test_even_number_with_even_set_bits(self):
        self.assertEqual(count_With_Odd_SetBits(8), 4)

    def test_negative_number(self):
        self.assertEqual(count_With_Odd_SetBits(-5), -5)

    def test_zero(self):
        self.assertEqual(count_With_Odd_SetBits(0), 0)
