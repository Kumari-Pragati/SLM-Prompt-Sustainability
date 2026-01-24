import unittest
from mbpp_78_code import count_With_Odd_SetBits

class TestCountWithOddSetBits(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(count_With_Odd_SetBits(3), 1)
        self.assertEqual(count_With_Odd_SetBits(5), 2)
        self.assertEqual(count_With_Odd_SetBits(7), 3)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_With_Odd_SetBits(0), 0)
        self.assertEqual(count_With_Odd_SetBits(1), 0)
        self.assertEqual(count_With_Odd_SetBits(2), 1)
        self.assertEqual(count_With_Odd_SetBits(4), 2)
        self.assertEqual(count_With_Odd_SetBits(8), 4)
        self.assertEqual(count_With_Odd_SetBits(9), 4)

    def test_odd_set_bits_and_even_input(self):
        self.assertEqual(count_With_Odd_SetBits(6), 3)

    def test_invalid_input(self):
        self.assertRaises(TypeError, count_With_Odd_SetBits, 'string')
        self.assertRaises(TypeError, count_With_Odd_SetBits, -1)
        self.assertRaises(TypeError, count_With_Odd_SetBits, float('inf'))
        self.assertRaises(TypeError, count_With_Odd_SetBits, complex(1, 2))
