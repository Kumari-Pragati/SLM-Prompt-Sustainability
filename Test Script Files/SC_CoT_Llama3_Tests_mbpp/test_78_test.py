import unittest
from mbpp_78_code import count_With_Odd_SetBits

class TestCountWithOddSetBits(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(count_With_Odd_SetBits(5), 2)
        self.assertEqual(count_With_Odd_SetBits(10), 5)
        self.assertEqual(count_With_Odd_SetBits(15), 8)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(count_With_Odd_SetBits(0), 0)
        self.assertEqual(count_With_Odd_SetBits(1), 0)
        self.assertEqual(count_With_Odd_SetBits(2), 1)
        self.assertEqual(count_With_Odd_SetBits(3), 1)
        self.assertEqual(count_With_Odd_SetBits(4), 2)
        self.assertEqual(count_With_Odd_SetBits(5), 2)
        self.assertEqual(count_With_Odd_SetBits(6), 3)
        self.assertEqual(count_With_Odd_SetBits(7), 3)
        self.assertEqual(count_With_Odd_SetBits(8), 4)
        self.assertEqual(count_With_Odd_SetBits(9), 4)
        self.assertEqual(count_With_Odd_SetBits(10), 5)

    def test_special_and_corner_cases(self):
        self.assertEqual(count_With_Odd_SetBits(11), 5)
        self.assertEqual(count_With_Odd_SetBits(12), 6)
        self.assertEqual(count_With_Odd_SetBits(13), 6)
        self.assertEqual(count_With_Odd_SetBits(14), 7)
        self.assertEqual(count_With_Odd_SetBits(15), 8)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_With_Odd_SetBits('a')
