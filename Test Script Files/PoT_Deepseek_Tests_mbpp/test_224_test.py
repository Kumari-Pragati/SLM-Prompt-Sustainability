import unittest
from mbpp_224_code import count_Set_Bits

class TestCountSetBits(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_Set_Bits(0), 0)
        self.assertEqual(count_Set_Bits(1), 1)
        self.assertEqual(count_Set_Bits(2), 1)
        self.assertEqual(count_Set_Bits(3), 2)
        self.assertEqual(count_Set_Bits(4), 1)
        self.assertEqual(count_Set_Bits(7), 3)
        self.assertEqual(count_Set_Bits(8), 1)

    def test_edge_cases(self):
        self.assertEqual(count_Set_Bits(255), 8)
        self.assertEqual(count_Set_Bits(511), 9)

    def test_boundary_cases(self):
        self.assertEqual(count_Set_Bits(2**31 - 1), 31)
        self.assertEqual(count_Set_Bits(2**31), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_Set_Bits('invalid')
        with self.assertRaises(TypeError):
            count_Set_Bits(None)
