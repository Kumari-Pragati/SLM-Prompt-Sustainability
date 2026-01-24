import unittest
from mbpp_6_code import differ_At_One_Bit_Pos

class TestDifferAtOneBitPos(unittest.TestCase):

    def test_differ_at_one_bit_typical(self):
        # Typical case: two numbers that differ at one bit
        self.assertEqual(differ_At_One_Bit_Pos(5, 6), True)
        self.assertEqual(differ_At_One_Bit_Pos(10, 11), True)
        self.assertEqual(differ_At_One_Bit_Pos(20, 21), True)

    def test_differ_at_one_bit_edge(self):
        # Edge case: two numbers that differ at the most significant bit
        self.assertEqual(differ_At_One_Bit_Pos(1, 2), True)
        self.assertEqual(differ_At_One_Bit_Pos(127, 128), True)
        self.assertEqual(differ_At_One_Bit_Pos(127, 126), True)

    def test_differ_at_one_bit_boundary(self):
        # Boundary case: two numbers that differ at the least significant bit
        self.assertEqual(differ_At_One_Bit_Pos(1, 2), True)
        self.assertEqual(differ_At_One_Bit_Pos(2**31 - 1, 2**31), True)
        self.assertEqual(differ_At_One_Bit_Pos(2**31, 2**31 - 1), True)

    def test_differ_at_one_bit_error(self):
        # Error case: non-integer inputs
        self.assertRaises(TypeError, differ_At_One_Bit_Pos, 3.14, 'a')
        self.assertRaises(TypeError, differ_At_One_Bit_Pos, 'b', 3)

    def test_differ_at_one_bit_power_of_two(self):
        # Error case: both inputs are powers of two
        self.assertRaises(AssertionError, differ_At_One_Bit_Pos, 4, 8)
        self.assertRaises(AssertionError, differ_At_One_Bit_Pos, 16, 32)
        self.assertRaises(AssertionError, differ_At_One_Bit_Pos, 2**10, 2**10)
