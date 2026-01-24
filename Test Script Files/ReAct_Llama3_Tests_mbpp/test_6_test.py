import unittest
from mbpp_6_code import differ_At_One_Bit_Pos

class TestDifferAtOneBitPos(unittest.TestCase):
    def test_power_of_two(self):
        self.assertTrue(differ_At_One_Bit_Pos(8, 4))
        self.assertFalse(differ_At_One_Bit_Pos(5, 3))

    def test_non_power_of_two(self):
        self.assertFalse(differ_At_One_Bit_Pos(10, 6))
        self.assertFalse(differ_At_One_Bit_Pos(7, 5))

    def test_edge_cases(self):
        self.assertFalse(differ_At_One_Bit_Pos(0, 0))
        self.assertFalse(differ_At_One_Bit_Pos(1, 1))

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            differ_At_One_Bit_Pos('a', 'b')
