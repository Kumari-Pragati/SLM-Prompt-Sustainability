import unittest
from mbpp_671_code import set_Right_most_Unset_Bit

class TestSetRightmostUnsetBit(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(set_Right_most_Unset_Bit(10), 12)

    def test_edge_case_zero(self):
        self.assertEqual(set_Right_most_Unset_Bit(0), 1)

    def test_boundary_case_max_int(self):
        self.assertEqual(set_Right_most_Unset_Bit(2147483647), 2147483648)

    def test_boundary_case_min_int(self):
        self.assertEqual(set_Right_most_Unset_Bit(-2147483648), -2147483647)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            set_Right_most_Unset_Bit("invalid")
