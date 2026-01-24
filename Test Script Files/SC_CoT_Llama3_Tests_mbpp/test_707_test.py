import unittest
from mbpp_707_code import count_Set_Bits

class TestCountSetBits(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(count_Set_Bits(1), 1)
        self.assertEqual(count_Set_Bits(2), 2)
        self.assertEqual(count_Set_Bits(3), 2)
        self.assertEqual(count_Set_Bits(4), 2)
        self.assertEqual(count_Set_Bits(5), 3)
        self.assertEqual(count_Set_Bits(6), 3)
        self.assertEqual(count_Set_Bits(7), 3)
        self.assertEqual(count_Set_Bits(8), 3)

    def test_edge_cases(self):
        self.assertEqual(count_Set_Bits(0), 0)
        self.assertEqual(count_Set_Bits(9), 3)
        self.assertEqual(count_Set_Bits(10), 3)
        self.assertEqual(count_Set_Bits(11), 4)
        self.assertEqual(count_Set_Bits(12), 4)
        self.assertEqual(count_Set_Bits(13), 4)
        self.assertEqual(count_Set_Bits(14), 4)

    def test_boundary_cases(self):
        self.assertEqual(count_Set_Bits(15), 4)
        self.assertEqual(count_Set_Bits(16), 4)
        self.assertEqual(count_Set_Bits(17), 5)
        self.assertEqual(count_Set_Bits(18), 5)
        self.assertEqual(count_Set_Bits(19), 5)
        self.assertEqual(count_Set_Bits(20), 5)

    def test_special_cases(self):
        self.assertEqual(count_Set_Bits(21), 5)
        self.assertEqual(count_Set_Bits(22), 5)
        self.assertEqual(count_Set_Bits(23), 5)
        self.assertEqual(count_Set_Bits(24), 5)
        self.assertEqual(count_Set_Bits(25), 5)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_Set_Bits("a")
        with self.assertRaises(TypeError):
            count_Set_Bits(None)
