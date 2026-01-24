import unittest
from mbpp_78_code import count_With_Odd_SetBits

class TestCountWithOddSetBits(unittest.TestCase):

    def test_even_numbers(self):
        self.assertEqual(count_With_Odd_SetBits(4), 2)

    def test_odd_numbers(self):
        self.assertEqual(count_With_Odd_SetBits(5), 2)

    def test_edge_case_zero(self):
        self.assertEqual(count_With_Odd_SetBits(0), 0)

    def test_edge_case_one(self):
        self.assertEqual(count_With_Odd_SetBits(1), 1)

    def test_edge_case_negative(self):
        with self.assertRaises(TypeError):
            count_With_Odd_SetBits(-1)

    def test_edge_case_large_number(self):
        self.assertEqual(count_With_Odd_SetBits(1000000), 500000)

    def test_edge_case_binary_string(self):
        with self.assertRaises(TypeError):
            count_With_Odd_SetBits('101010')
