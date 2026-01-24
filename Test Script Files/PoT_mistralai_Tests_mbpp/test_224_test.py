import unittest
from mbpp_224_code import count_Set_Bits

class TestCountSetBits(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(count_Set_Bits(0), 0)
        self.assertEqual(count_Set_Bits(1), 1)
        self.assertEqual(count_Set_Bits(3), 2)
        self.assertEqual(count_Set_Bits(10), 3)
        self.assertEqual(count_Set_Bits(12345), 17)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(count_Set_Bits(-1), 31)
        self.assertEqual(count_Set_Bits(0b1000_0000), 1)
        self.assertEqual(count_Set_Bits(0xFFFFFFFF), 32)
        self.assertEqual(count_Set_Bits(0), 0)
        self.assertEqual(count_Set_Bits(1 << 31), 1)
