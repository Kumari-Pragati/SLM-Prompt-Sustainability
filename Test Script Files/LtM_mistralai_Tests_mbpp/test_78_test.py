import unittest
from mbpp_78_code import count_With_Odd_SetBits

class TestCountWithOddSetBits(unittest.TestCase):

    def test_simple_odd_numbers(self):
        self.assertEqual(count_With_Odd_SetBits(1), 0.5)
        self.assertEqual(count_With_Odd_SetBits(3), 1.5)
        self.assertEqual(count_With_Odd_SetBits(5), 2.5)

    def test_simple_even_numbers(self):
        self.assertEqual(count_With_Odd_SetBits(2), 1)
        self.assertEqual(count_With_Odd_SetBits(4), 2)
        self.assertEqual(count_With_Odd_SetBits(6), 3)

    def test_edge_cases(self):
        self.assertEqual(count_With_Odd_SetBits(0), 0)
        self.assertEqual(count_With_Odd_SetBits(1 << 31), 2147483647 // 2)

    def test_special_cases(self):
        self.assertEqual(count_With_Odd_SetBits(1 << 63), 2**63 // 2)
