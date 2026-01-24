import unittest
from mbpp_957_code import get_First_Set_Bit_Pos

class TestGetFirstSetBitPos(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(get_First_Set_Bit_Pos(8), 1)

    def test_edge_case_zero(self):
        with self.assertRaises(ZeroDivisionError):
            get_First_Set_Bit_Pos(0)

    def test_edge_case_one(self):
        self.assertEqual(get_First_Set_Bit_Pos(1), 1)

    def test_edge_case_power_of_two(self):
        self.assertEqual(get_First_Set_Bit_Pos(8), 1)

    def test_edge_case_power_of_two_minus_one(self):
        self.assertEqual(get_First_Set_Bit_Pos(7), 1)

    def test_edge_case_power_of_two_plus_one(self):
        self.assertEqual(get_First_Set_Bit_Pos(9), 2)

    def test_edge_case_power_of_two_times_two(self):
        self.assertEqual(get_First_Set_Bit_Pos(16), 2)

    def test_edge_case_power_of_two_times_two_minus_one(self):
        self.assertEqual(get_First_Set_Bit_Pos(15), 2)

    def test_edge_case_power_of_two_times_two_plus_one(self):
        self.assertEqual(get_First_Set_Bit_Pos(17), 3)

    def test_edge_case_power_of_two_times_three(self):
        self.assertEqual(get_First_Set_Bit_Pos(32), 3)

    def test_edge_case_power_of_two_times_three_minus_one(self):
        self.assertEqual(get_First_Set_Bit_Pos(31), 3)

    def test_edge_case_power_of_two_times_three_plus_one(self):
        self.assertEqual(get_First_Set_Bit_Pos(33), 4)
