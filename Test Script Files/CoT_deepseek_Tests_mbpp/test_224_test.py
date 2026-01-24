import unittest
from mbpp_224_code import count_Set_Bits

class TestCountSetBits(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Set_Bits(10), 2)

    def test_zero(self):
        self.assertEqual(count_Set_Bits(0), 0)

    def test_boundary_conditions(self):
        self.assertEqual(count_Set_Bits(1), 1)
        self.assertEqual(count_Set_Bits(2), 1)
        self.assertEqual(count_Set_Bits(3), 2)
        self.assertEqual(count_Set_Bits(4), 1)
        self.assertEqual(count_Set_Bits(8), 1)
        self.assertEqual(count_Set_Bits(16), 1)

    def test_large_number(self):
        self.assertEqual(count_Set_Bits(1023), 9)

    def test_negative_number(self):
        with self.assertRaises(Exception):
            count_Set_Bits(-10)

    def test_non_integer_input(self):
        with self.assertRaises(Exception):
            count_Set_Bits(10.5)
