import unittest
from mbpp_707_code import count_Set_Bits

class TestCountSetBits(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_Set_Bits(1), 1)
        self.assertEqual(count_Set_Bits(2), 2)
        self.assertEqual(count_Set_Bits(3), 2)
        self.assertEqual(count_Set_Bits(4), 3)
        self.assertEqual(count_Set_Bits(5), 3)
        self.assertEqual(count_Set_Bits(6), 4)
        self.assertEqual(count_Set_Bits(7), 4)
        self.assertEqual(count_Set_Bits(8), 5)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(count_Set_Bits(0), 0)
        self.assertEqual(count_Set_Bits(1), 1)
        self.assertEqual(count_Set_Bits(2**31 - 1), 31)
        self.assertEqual(count_Set_Bits(2**31), 32)

    def test_corner_cases(self):
        self.assertEqual(count_Set_Bits(2**31 - 2), 30)
        self.assertEqual(count_Set_Bits(2**31 - 3), 30)
        self.assertEqual(count_Set_Bits(2**31 - 4), 30)
        self.assertEqual(count_Set_Bits(2**31 - 5), 30)
