import unittest
from mbpp_224_code import count_Set_Bits

class TestCountSetBits(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(count_Set_Bits(0), 0)
        self.assertEqual(count_Set_Bits(1), 1)
        self.assertEqual(count_Set_Bits(2), 1)
        self.assertEqual(count_Set_Bits(3), 2)
        self.assertEqual(count_Set_Bits(4), 1)
        self.assertEqual(count_Set_Bits(5), 2)
        self.assertEqual(count_Set_Bits(6), 2)
        self.assertEqual(count_Set_Bits(7), 3)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(count_Set_Bits(8), 1)
        self.assertEqual(count_Set_Bits(9), 2)
        self.assertEqual(count_Set_Bits(10), 1)
        self.assertEqual(count_Set_Bits(11), 2)
        self.assertEqual(count_Set_Bits(12), 2)
        self.assertEqual(count_Set_Bits(13), 3)
        self.assertEqual(count_Set_Bits(14), 1)
        self.assertEqual(count_Set_Bits(15), 4)

    def test_corner_cases(self):
        self.assertEqual(count_Set_Bits(16), 1)
        self.assertEqual(count_Set_Bits(17), 2)
        self.assertEqual(count_Set_Bits(18), 2)
        self.assertEqual(count_Set_Bits(19), 3)
        self.assertEqual(count_Set_Bits(20), 1)
        self.assertEqual(count_Set_Bits(21), 2)
        self.assertEqual(count_Set_Bits(22), 2)
        self.assertEqual(count_Set_Bits(23), 3)
