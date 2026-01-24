import unittest
from mbpp_78_code import count_With_Odd_SetBits

class TestCountWithOddSetBits(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(count_With_Odd_SetBits(1), 1)
        self.assertEqual(count_With_Odd_SetBits(2), 1)
        self.assertEqual(count_With_Odd_SetBits(3), 2)
        self.assertEqual(count_With_Odd_SetBits(4), 2)
        self.assertEqual(count_With_Odd_SetBits(5), 2)
        self.assertEqual(count_With_Odd_SetBits(6), 2)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(count_With_Odd_SetBits(0), 0)
        self.assertEqual(count_With_Odd_SetBits(1), 1)
        self.assertEqual(count_With_Odd_SetBits(2), 1)
        self.assertEqual(count_With_Odd_SetBits(3), 2)
        self.assertEqual(count_With_Odd_SetBits(4), 2)
        self.assertEqual(count_With_Odd_SetBits(5), 2)
        self.assertEqual(count_With_Odd_SetBits(6), 2)
        self.assertEqual(count_With_Odd_SetBits(7), 2)
        self.assertEqual(count_With_Odd_SetBits(8), 2)

    def test_corner_cases(self):
        self.assertEqual(count_With_Odd_SetBits(9), 2)
        self.assertEqual(count_With_Odd_SetBits(10), 2)
        self.assertEqual(count_With_Odd_SetBits(11), 2)
        self.assertEqual(count_With_Odd_SetBits(12), 2)
        self.assertEqual(count_With_Odd_SetBits(13), 2)
        self.assertEqual(count_With_Odd_SetBits(14), 2)
        self.assertEqual(count_With_Odd_SetBits(15), 2)
