import unittest
from mbpp_707_code import count_Set_Bits

class TestCountSetBits(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(count_Set_Bits(10), 3)
        self.assertEqual(count_Set_Bits(20), 7)
        self.assertEqual(count_Set_Bits(30), 10)

    def test_edge_cases(self):
        self.assertEqual(count_Set_Bits(0), 0)
        self.assertEqual(count_Set_Bits(1), 1)
        self.assertEqual(count_Set_Bits(2**31 - 1), 31)

    def test_boundary_conditions(self):
        self.assertEqual(count_Set_Bits(2**31), 32)
        self.assertEqual(count_Set_Bits(2**63 - 1), 64)

    def test_special_cases(self):
        self.assertEqual(count_Set_Bits(2), 1)
        self.assertEqual(count_Set_Bits(3), 1)
        self.assertEqual(count_Set_Bits(4), 2)
