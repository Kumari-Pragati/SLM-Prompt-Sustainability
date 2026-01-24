import unittest
from mbpp_707_code import count_Set_Bits

class TestCountSetBits(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_Set_Bits(10), 4)

    def test_boundary_conditions(self):
        self.assertEqual(count_Set_Bits(0), 0)
        self.assertEqual(count_Set_Bits(1), 1)
        self.assertEqual(count_Set_Bits(2), 1)
        self.assertEqual(count_Set_Bits(3), 2)

    def test_edge_cases(self):
        self.assertEqual(count_Set_Bits(255), 8)
        self.assertEqual(count_Set_Bits(1023), 10)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_Set_Bits('10')
        with self.assertRaises(TypeError):
            count_Set_Bits(None)
