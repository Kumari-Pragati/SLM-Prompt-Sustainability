import unittest
from mbpp_707_code import count_Set_Bits

class TestCountSetBits(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(count_Set_Bits(0), 0)
        self.assertEqual(count_Set_Bits(1), 1)
        self.assertEqual(count_Set_Bits(3), 2)
        self.assertEqual(count_Set_Bits(4), 1)
        self.assertEqual(count_Set_Bits(5), 2)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_Set_Bits(127), 7)
        self.assertEqual(count_Set_Bits(128), 1)
        self.assertEqual(count_Set_Bits(129), 2)
        self.assertEqual(count_Set_Bits(2147483647), 31)
        self.assertEqual(count_Set_Bits(2147483648), 1)

    def test_complex_scenarios(self):
        self.assertEqual(count_Set_Bits(1023), 10)
        self.assertEqual(count_Set_Bits(1024), 1)
        self.assertEqual(count_Set_Bits(1025), 2)
        self.assertEqual(count_Set_Bits(2147483643), 30)
        self.assertEqual(count_Set_Bits(2147483644), 1)
        self.assertEqual(count_Set_Bits(2147483645), 2)
        self.assertEqual(count_Set_Bits(2147483646), 3)
