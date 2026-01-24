import unittest
from707_code import count_Set_Bits

class TestCountSetBits(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(count_Set_Bits(0), 0)
        self.assertEqual(count_Set_Bits(1), 1)
        self.assertEqual(count_Set_Bits(3), 2)
        self.assertEqual(count_Set_Bits(5), 3)
        self.assertEqual(count_Set_Bits(15), 4)
        self.assertEqual(count_Set_Bits(255), 8)
        self.assertEqual(count_Set_Bits(256), 9)
        self.assertEqual(count_Set_Bits(257), 9)
        self.assertEqual(count_Set_Bits(1023), 10)
        self.assertEqual(count_Set_Bits(1024), 11)
        self.assertEqual(count_Set_Bits(1025), 11)
        self.assertEqual(count_Set_Bits(16383), 17)
        self.assertEqual(count_Set_Bits(16384), 18)
        self.assertEqual(count_Set_Bits(16385), 18)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_Set_Bits(-1), 32)
        self.assertEqual(count_Set_Bits(0b1000_0000), 1)
        self.assertEqual(count_Set_Bits(0b1111_1111), 16)
        self.assertEqual(count_Set_Bits(0b1000000000), 31)
        self.assertEqual(count_Set_Bits(0b11111111111111111111), 64)
        self.assertEqual(count_Set_Bits(0xFFFFFFFF), 32)
        self.assertEqual(count_Set_Bits(0xFFFFFFFFF), 33)
        self.assertEqual(count_Set_Bits(0b10000000000000000000000000000001), 64)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, count_Set_Bits, "not_an_integer")
        self.assertRaises(TypeError, count_Set_Bits, 3.14)
        self.assertRaises(TypeError, count_Set_Bits, (1, 2, 3))
        self.assertRaises(TypeError, count_Set_Bits, [1, 2, 3])
