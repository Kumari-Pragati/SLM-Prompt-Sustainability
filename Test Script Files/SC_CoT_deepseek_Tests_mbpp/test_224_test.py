import unittest
from mbpp_224_code import count_Set_Bits

class TestCountSetBits(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_Set_Bits(0), 0)
        self.assertEqual(count_Set_Bits(1), 1)
        self.assertEqual(count_Set_Bits(2), 1)
        self.assertEqual(count_Set_Bits(3), 2)
        self.assertEqual(count_Set_Bits(8), 1)

    def test_boundary_conditions(self):
        self.assertEqual(count_Set_Bits(2**31 - 1), 31)
        self.assertEqual(count_Set_Bits(2**31), 32)

    def test_edge_cases(self):
        self.assertEqual(count_Set_Bits(2**32 - 1), 32)
        self.assertEqual(count_Set_Bits(2**32), 32)

    def test_special_cases(self):
        self.assertEqual(count_Set_Bits(1023), 9)
        self.assertEqual(count_Set_Bits(1024), 1)
        self.assertEqual(count_Set_Bits(2047), 11)
        self.assertEqual(count_Set_Bits(2048), 1)
