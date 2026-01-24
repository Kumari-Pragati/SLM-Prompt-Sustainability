import unittest
from mbpp_78_code import count_With_Odd_SetBits

class TestCountWithOddSetBits(unittest.TestCase):

    def test_simple_cases(self):
        self.assertEqual(count_With_Odd_SetBits(1), 1)
        self.assertEqual(count_With_Odd_SetBits(2), 2)
        self.assertEqual(count_With_Odd_SetBits(3), 2)
        self.assertEqual(count_With_Odd_SetBits(4), 2)
        self.assertEqual(count_With_Odd_SetBits(5), 3)
        self.assertEqual(count_With_Odd_SetBits(6), 3)
        self.assertEqual(count_With_Odd_SetBits(7), 3)
        self.assertEqual(count_With_Odd_SetBits(8), 4)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_With_Odd_SetBits(0), 0)
        self.assertEqual(count_With_Odd_SetBits(9), 4)
        self.assertEqual(count_With_Odd_SetBits(10), 5)
        self.assertEqual(count_With_Odd_SetBits(11), 5)
        self.assertEqual(count_With_Odd_SetBits(12), 5)
        self.assertEqual(count_With_Odd_SetBits(13), 5)
        self.assertEqual(count_With_Odd_SetBits(14), 6)
        self.assertEqual(count_With_Odd_SetBits(15), 6)
        self.assertEqual(count_With_Odd_SetBits(16), 8)

    def test_more_complex_cases(self):
        self.assertEqual(count_With_Odd_SetBits(17), 8)
        self.assertEqual(count_With_Odd_SetBits(18), 8)
        self.assertEqual(count_With_Odd_SetBits(19), 8)
        self.assertEqual(count_With_Odd_SetBits(20), 8)
        self.assertEqual(count_With_Odd_SetBits(21), 9)
        self.assertEqual(count_With_Odd_SetBits(22), 9)
        self.assertEqual(count_With_Odd_SetBits(23), 9)
        self.assertEqual(count_With_Odd_SetBits(24), 9)
