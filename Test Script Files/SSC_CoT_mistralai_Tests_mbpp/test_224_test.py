import unittest
from mbpp_224_code import count_Set_Bits

class TestCountSetBits(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(count_Set_Bits(3), 2)
        self.assertEqual(count_Set_Bits(10), 3)
        self.assertEqual(count_Set_Bits(255), 8)
        self.assertEqual(count_Set_Bits(65280), 16)
        self.assertEqual(count_Set_Bits(16777215), 32)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_Set_Bits(0), 0)
        self.assertEqual(count_Set_Bits(1), 1)
        self.assertEqual(count_Set_Bits(2147483647), 31)
        self.assertEqual(count_Set_Bits(-1), 32)
        self.assertEqual(count_Set_Bits(2**64 - 1), 64)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, count_Set_Bits, 'invalid_input')
        self.assertRaises(TypeError, count_Set_Bits, 2.5)
        self.assertRaises(TypeError, count_Set_Bits, [1, 2, 3])
