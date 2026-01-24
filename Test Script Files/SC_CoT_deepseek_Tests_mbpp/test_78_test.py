import unittest

from mbpp_78_code import count_With_Odd_SetBits

class TestCountWithOddSetBits(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_With_Odd_SetBits(10), 6)

    def test_edge_case_with_odd_number(self):
        self.assertEqual(count_With_Odd_SetBits(7), 4)

    def test_edge_case_with_even_number(self):
        self.assertEqual(count_With_Odd_SetBits(8), 4)

    def test_boundary_case_with_zero(self):
        self.assertEqual(count_With_Odd_SetBits(0), 0)

    def test_boundary_case_with_negative_number(self):
        with self.assertRaises(ValueError):
            count_With_Odd_SetBits(-5)

    def test_corner_case_with_max_integer(self):
        with self.assertRaises(OverflowError):
            count_With_Odd_SetBits(2**31 - 1)

    def test_corner_case_with_min_integer(self):
        with self.assertRaises(OverflowError):
            count_With_Odd_SetBits(-2**31)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            count_With_Odd_SetBits('abc')
