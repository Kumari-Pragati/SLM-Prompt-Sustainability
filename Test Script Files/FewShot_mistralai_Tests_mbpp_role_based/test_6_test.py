import unittest
from mbpp_6_code import differ_At_One_Bit_Pos

class TestDifferAtOneBitPos(unittest.TestCase):
    def test_differ_at_one_bit_pos_power_of_two(self):
        self.assertEqual(differ_At_One_Bit_Pos(2, 4), True)
        self.assertEqual(differ_At_One_Bit_Pos(4, 8), True)
        self.assertEqual(differ_At_One_Bit_Pos(8, 16), True)

    def test_differ_at_one_bit_pos_non_power_of_two(self):
        self.assertEqual(differ_At_One_Bit_Pos(3, 4), True)
        self.assertEqual(differ_At_One_Bit_Pos(5, 6), False)
        self.assertEqual(differ_At_One_Bit_Pos(7, 8), True)

    def test_differ_at_one_bit_pos_zero(self):
        self.assertEqual(differ_At_One_Bit_Pos(0, 0), False)

    def test_differ_at_one_bit_pos_negative(self):
        self.assertEqual(differ_At_One_Bit_Pos(-2, -4), True)
        self.assertEqual(differ_At_One_Bit_Pos(-4, -8), True)
        self.assertEqual(differ_At_One_Bit_Pos(-8, -16), True)
