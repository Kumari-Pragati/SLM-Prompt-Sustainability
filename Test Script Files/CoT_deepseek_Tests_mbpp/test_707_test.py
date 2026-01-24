import unittest
from mbpp_707_code import count_Set_Bits

class TestCountSetBits(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Set_Bits(10), 4)

    def test_zero_input(self):
        self.assertEqual(count_Set_Bits(0), 0)

    def test_negative_input(self):
        with self.assertRaises(Exception):
            count_Set_Bits(-5)

    def test_large_number(self):
        self.assertEqual(count_Set_Bits(1000000), 325000)

    def test_boundary_conditions(self):
        self.assertEqual(count_Set_Bits(1), 1)
        self.assertEqual(count_Set_Bits(2), 2)
        self.assertEqual(count_Set_Bits(4), 1)
