import unittest
from mbpp_707_code import count_Set_Bits

class TestCountSetBits(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(count_Set_Bits(0), 0)

    def test_one(self):
        self.assertEqual(count_Set_Bits(1), 1)

    def test_power_of_two(self):
        self.assertEqual(count_Set_Bits(2), 1)
        self.assertEqual(count_Set_Bits(4), 2)
        self.assertEqual(count_Set_Bits(8), 3)
        self.assertEqual(count_Set_Bits(16), 4)

    def test_power_of_two_plus_one(self):
        self.assertEqual(count_Set_Bits(3), 2)
        self.assertEqual(count_Set_Bits(5), 2)
        self.assertEqual(count_Set_Bits(9), 3)
        self.assertEqual(count_Set_Bits(17), 4)

    def test_random_numbers(self):
        self.assertEqual(count_Set_Bits(10), 2)
        self.assertEqual(count_Set_Bits(15), 4)
        self.assertEqual(count_Set_Bits(20), 4)
        self.assertEqual(count_Set_Bits(25), 5)

    def test_edge_cases(self):
        self.assertEqual(count_Set_Bits(2**31 - 1), 31)
        self.assertEqual(count_Set_Bits(2**31), 31)
