import unittest
from78_code import count_With_Odd_SetBits

class TestCountWithOddSetBits(unittest.TestCase):
    def test_positive_odd(self):
        self.assertEqual(count_With_Odd_SetBits(1), 0.5)
        self.assertEqual(count_With_Odd_SetBits(3), 1)
        self.assertEqual(count_With_Odd_SetBits(5), 2)

    def test_positive_even(self):
        self.assertEqual(count_With_Odd_SetBits(2), 1)
        self.assertEqual(count_With_Odd_SetBits(4), 2)
        self.assertEqual(count_With_Odd_SetBits(6), 3)

    def test_zero(self):
        self.assertEqual(count_With_Odd_SetBits(0), 0)

    def test_negative(self):
        self.assertEqual(count_With_Odd_SetBits(-1), 0)
        self.assertEqual(count_With_Odd_SetBits(-3), 0)

    def test_large_numbers(self):
        self.assertEqual(count_With_Odd_SetBits(2 ** 16 - 1), 2 ** 15)
        self.assertEqual(count_With_Odd_SetBits(2 ** 16), 2 ** 15 + 1)
        self.assertEqual(count_With_Odd_SetBits(2 ** 17 - 1), 2 ** 16)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            count_With_Odd_SetBits(float('nan'))
        with self.assertRaises(ValueError):
            count_With_Odd_SetBits(float('inf'))
        with self.assertRaises(ValueError):
            count_With_Odd_SetBits(-2 ** 31)
