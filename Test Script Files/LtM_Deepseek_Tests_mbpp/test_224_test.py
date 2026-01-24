import unittest
from mbpp_224_code import count_Set_Bits

class TestCountSetBits(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(count_Set_Bits(0), 0)
        self.assertEqual(count_Set_Bits(1), 1)
        self.assertEqual(count_Set_Bits(2), 1)
        self.assertEqual(count_Set_Bits(3), 2)
        self.assertEqual(count_Set_Bits(4), 1)
        self.assertEqual(count_Set_Bits(5), 2)
        self.assertEqual(count_Set_Bits(6), 2)
        self.assertEqual(count_Set_Bits(7), 3)
        self.assertEqual(count_Set_Bits(8), 1)

    def test_edge_conditions(self):
        self.assertEqual(count_Set_Bits(2**31 - 1), 31)
        self.assertEqual(count_Set_Bits(2**31), 0)
        self.assertEqual(count_Set_Bits(2**63 - 1), 63)
        self.assertEqual(count_Set_Bits(2**63), 0)

    def test_complex_cases(self):
        self.assertEqual(count_Set_Bits(2**31 + 1), 32)
        self.assertEqual(count_Set_Bits(2**63 + 1), 64)
