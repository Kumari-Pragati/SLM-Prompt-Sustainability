import unittest
from mbpp_78_code import count_With_Odd_SetBits

class TestCountWithOddSetBits(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_With_Odd_SetBits(10), 5)
        self.assertEqual(count_With_Odd_SetBits(15), 8)
        self.assertEqual(count_With_Odd_SetBits(20), 10)

    def test_edge_cases(self):
        self.assertEqual(count_With_Odd_SetBits(0), 0)
        self.assertEqual(count_With_Odd_SetBits(1), 1)

    def test_boundary_cases(self):
        self.assertEqual(count_With_Odd_SetBits(2), 1)
        self.assertEqual(count_With_Odd_SetBits(3), 2)

    def test_odd_set_bits(self):
        self.assertEqual(count_With_Odd_SetBits(7), 4)
        self.assertEqual(count_With_Odd_SetBits(9), 5)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_With_Odd_SetBits('invalid')
