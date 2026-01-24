import unittest
from mbpp_224_code import count_Set_Bits

class TestCountSetBits(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_Set_Bits(10), 2)

    def test_boundary_conditions(self):
        self.assertEqual(count_Set_Bits(0), 0)
        self.assertEqual(count_Set_Bits(2**31 - 1), 31)

    def test_edge_cases(self):
        self.assertEqual(count_Set_Bits(2**31), 0)
        self.assertEqual(count_Set_Bits(2**31 - 1), 31)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_Set_Bits('invalid')
