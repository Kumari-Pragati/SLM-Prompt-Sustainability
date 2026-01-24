import unittest
from mbpp_707_code import count_Set_Bits

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
        self.assertEqual(count_Set_Bits(8), 1)

    def test_edge_cases(self):
        self.assertEqual(count_Set_Bits(255), 8)
        self.assertEqual(count_Set_Bits(511), 9)
        self.assertEqual(count_Set_Bits(1023), 10)

    def test_boundary_cases(self):
        self.assertEqual(count_Set_Bits(256), 1)
        self.assertEqual(count_Set_Bits(1024), 1)

    def test_corner_cases(self):
        self.assertEqual(count_Set_Bits(32767), 15)
        self.assertEqual(count_Set_Bits(65535), 16)
