import unittest
from mbpp_224_code import count_Set_Bits

class TestCountSetBits(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(count_Set_Bits(5), 2)
        self.assertEqual(count_Set_Bits(10), 2)
        self.assertEqual(count_Set_Bits(15), 4)

    def test_edge_cases(self):
        self.assertEqual(count_Set_Bits(0), 0)
        self.assertEqual(count_Set_Bits(1), 1)
        self.assertEqual(count_Set_Bits(2**31 - 1), 31)

    def test_boundary_cases(self):
        self.assertEqual(count_Set_Bits(2**31), 31)
        self.assertEqual(count_Set_Bits(2**32 - 1), 32)

    def test_corner_cases(self):
        self.assertEqual(count_Set_Bits(2**31 - 2), 30)
        self.assertEqual(count_Set_Bits(2**31 - 3), 30)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_Set_Bits('a')
