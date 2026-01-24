import unittest
from mbpp_78_code import count_With_Odd_SetBits

class TestCountWithOddSetBits(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_With_Odd_SetBits(1), 0.5)
        self.assertEqual(count_With_Odd_SetBits(3), 1.5)
        self.assertEqual(count_With_Odd_SetBits(5), 2.5)
        self.assertEqual(count_With_Odd_SetBits(7), 3.5)
        self.assertEqual(count_With_Odd_SetBits(9), 4.5)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(count_With_Odd_SetBits(0), 0)
        self.assertEqual(count_With_Odd_SetBits(1023), 511.5)
        self.assertEqual(count_With_Odd_SetBits(1024), 512)
        self.assertEqual(count_With_Odd_SetBits(1025), 512.5)
        self.assertEqual(count_With_Odd_SetBits(2147483647), 1073741823.5)
        self.assertEqual(count_With_Odd_SetBits(2147483648), 1073741824)
