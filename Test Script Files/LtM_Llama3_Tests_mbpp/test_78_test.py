import unittest
from mbpp_78_code import count_With_Odd_SetBits

class TestCountWithOddSetBits(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(count_With_Odd_SetBits(1), 1)
        self.assertEqual(count_With_Odd_SetBits(2), 1)
        self.assertEqual(count_With_Odd_SetBits(3), 2)
        self.assertEqual(count_With_Odd_SetBits(4), 2)
        self.assertEqual(count_With_Odd_SetBits(5), 2)
        self.assertEqual(count_With_Odd_SetBits(6), 2)

    def test_edge(self):
        self.assertEqual(count_With_Odd_SetBits(0), 0)
        self.assertEqual(count_With_Odd_SetBits(7), 3)
        self.assertEqual(count_With_Odd_SetBits(8), 4)
        self.assertEqual(count_With_Odd_SetBits(9), 4)
        self.assertEqual(count_With_Odd_SetBits(10), 5)

    def test_odd(self):
        self.assertEqual(count_With_Odd_SetBits(11), 5)
        self.assertEqual(count_With_Odd_SetBits(12), 6)
        self.assertEqual(count_With_Odd_SetBits(13), 6)
        self.assertEqual(count_With_Odd_SetBits(14), 7)
        self.assertEqual(count_With_Odd_SetBits(15), 7)

    def test_even(self):
        self.assertEqual(count_With_Odd_SetBits(16), 8)
        self.assertEqual(count_With_Odd_SetBits(17), 8)
        self.assertEqual(count_With_Odd_SetBits(18), 9)
        self.assertEqual(count_With_Odd_SetBits(19), 9)
        self.assertEqual(count_With_Odd_SetBits(20), 10)
