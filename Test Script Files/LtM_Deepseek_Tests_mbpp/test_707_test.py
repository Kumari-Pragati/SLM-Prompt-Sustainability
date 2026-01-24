import unittest
from mbpp_707_code import count_Set_Bits

class TestCountSetBits(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(count_Set_Bits(0), 0)
        self.assertEqual(count_Set_Bits(1), 1)
        self.assertEqual(count_Set_Bits(2), 1)
        self.assertEqual(count_Set_Bits(3), 2)
        self.assertEqual(count_Set_Bits(4), 1)

    def test_edge_conditions(self):
        self.assertEqual(count_Set_Bits(8), 1)
        self.assertEqual(count_Set_Bits(15), 4)
        self.assertEqual(count_Set_Bits(16), 1)
        self.assertEqual(count_Set_Bits(31), 5)
        self.assertEqual(count_Set_Bits(32), 1)

    def test_complex_cases(self):
        self.assertEqual(count_Set_Bits(1023), 10)
        self.assertEqual(count_Set_Bits(2047), 11)
        self.assertEqual(count_Set_Bits(4095), 12)
        self.assertEqual(count_Set_Bits(8191), 13)
        self.assertEqual(count_Set_Bits(16383), 14)
