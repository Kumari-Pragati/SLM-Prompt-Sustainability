import unittest
from mbpp_78_code import count_With_Odd_SetBits

class TestCountWithOddSetBits(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count_With_Odd_SetBits(10), 5)

    def test_edge_condition(self):
        self.assertEqual(count_With_Odd_SetBits(1), 1)

    def test_boundary_condition(self):
        self.assertEqual(count_With_Odd_SetBits(0), 0)

    def test_odd_set_bits(self):
        self.assertEqual(count_With_Odd_SetBits(7), 4)

    def test_even_set_bits(self):
        self.assertEqual(count_With_Odd_SetBits(8), 4)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_With_Odd_SetBits('invalid')
