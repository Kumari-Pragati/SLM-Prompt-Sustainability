import unittest
from mbpp_6_code import differ_At_One_Bit_Pos

class TestDifferAtOneBitPos(unittest.TestCase):
    def test_power_of_two(self):
        self.assertTrue(differ_At_One_Bit_Pos(8, 4))
        self.assertTrue(differ_At_One_Bit_Pos(16, 8))
        self.assertTrue(differ_At_One_Bit_Pos(32, 16))

    def test_non_power_of_two(self):
        self.assertFalse(differ_At_One_Bit_Pos(3, 1))
        self.assertFalse(differ_At_One_Bit_Pos(5, 1))
        self.assertFalse(differ_At_One_Bit_Pos(7, 3))

    def test_zero(self):
        self.assertFalse(differ_At_One_Bit_Pos(0, 0))

    def test_negative_numbers(self):
        self.assertFalse(differ_At_One_Bit_Pos(-8, -4))
        self.assertFalse(differ_At_One_Bit_Pos(-16, -8))
