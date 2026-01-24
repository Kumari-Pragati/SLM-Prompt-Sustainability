import unittest
from mbpp_224_code import count_Set_Bits

class TestCountSetBits(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(count_Set_Bits(0), 0)
        self.assertEqual(count_Set_Bits(1), 1)
        self.assertEqual(count_Set_Bits(3), 2)
        self.assertEqual(count_Set_Bits(15), 4)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_Set_Bits(-1), 31)
        self.assertEqual(count_Set_Bits(2**31 - 1), 31)
        self.assertEqual(count_Set_Bits(2**64 - 1), 63)

    def test_complex_inputs(self):
        self.assertEqual(count_Set_Bits(0b10000000), 1)
        self.assertEqual(count_Set_Bits(0b11111111), 8)
        self.assertEqual(count_Set_Bits(0b1010101010101010), 18)
