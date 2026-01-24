import unittest
from mbpp_6_code import bitwise_complement as bwc
from six_code import is_Power_Of_Two, differ_At_One_Bit_Pos

class TestIsPowerOfTwo(unittest.TestCase):
    def test_is_power_of_two_true(self):
        self.assertTrue(is_Power_Of_Two(1))
        self.assertTrue(is_Power_Of_Two(2))
        self.assertTrue(is_Power_Of_Two(4))
        self.assertTrue(is_Power_Of_Two(8))
        self.assertTrue(is_Power_Of_Two(16))

    def test_is_power_of_two_false(self):
        self.assertFalse(is_Power_Of_Two(3))
        self.assertFalse(is_Power_Of_Two(5))
        self.assertFalse(is_Power_Of_Two(7))
        self.assertFalse(is_Power_Of_Two(9))
        self.assertFalse(is_Power_Of_Two(10))

class TestDifferAtOneBitPos(unittest.TestCase):
    def test_differ_at_one_bit_pos_true(self):
        self.assertTrue(differ_At_One_Bit_Pos(1, 2))
        self.assertTrue(differ_At_One_Bit_Pos(3, 4))
        self.assertTrue(differ_At_One_Bit_Pos(5, 8))
        self.assertTrue(differ_At_One_Bit_Pos(10, 11))

    def test_differ_at_one_bit_pos_false(self):
        self.assertFalse(differ_At_One_Bit_Pos(1, 1))
        self.assertFalse(differ_At_One_Bit_Pos(2, 3))
        self.assertFalse(differ_At_One_Bit_Pos(4, 5))
        self.assertFalse(differ_At_One_Bit_Pos(8, 9))
        self.assertFalse(differ_At_One_Bit_Pos(11, 10))
