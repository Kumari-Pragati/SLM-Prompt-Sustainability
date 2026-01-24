import unittest
from mbpp_957_code import get_First_Set_Bit_Pos

class TestGetFirstSetBitPos(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(get_First_Set_Bit_Pos(18), 2)

    def test_edge_case_zero(self):
        self.assertEqual(get_First_Set_Bit_Pos(0), 0)

    def test_boundary_case_max_int(self):
        self.assertEqual(get_First_Set_Bit_Pos(2**31 - 1), 32)

    def test_boundary_case_min_int(self):
        self.assertEqual(get_First_Set_Bit_Pos(-2**31), 32)

    def test_invalid_input_negative(self):
        with self.assertRaises(ValueError):
            get_First_Set_Bit_Pos(-10)

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            get_First_Set_Bit_Pos(10.5)
