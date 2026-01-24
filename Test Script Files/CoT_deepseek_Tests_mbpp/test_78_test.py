import unittest
from mbpp_78_code import count_With_Odd_SetBits

class TestCountWithOddSetBits(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_With_Odd_SetBits(10), 6)
        self.assertEqual(count_With_Odd_SetBits(15), 9)
        self.assertEqual(count_With_Odd_SetBits(20), 11)

    def test_edge_cases(self):
        self.assertEqual(count_With_Odd_SetBits(0), 0)
        self.assertEqual(count_With_Odd_SetBits(1), 1)
        self.assertEqual(count_With_Odd_SetBits(2), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_With_Odd_SetBits('invalid')
        with self.assertRaises(TypeError):
            count_With_Odd_SetBits(None)
        with self.assertRaises(TypeError):
            count_With_Odd_SetBits(float('nan'))
