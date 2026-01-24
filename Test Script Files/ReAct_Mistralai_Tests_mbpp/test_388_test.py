import unittest
from mbpp_388_code import highest_Power_of_2

class TestHighestPowerOf2(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(highest_Power_of_2(1), 1)
        self.assertEqual(highest_Power_of_2(2), 2)
        self.assertEqual(highest_Power_of_2(4), 4)
        self.assertEqual(highest_Power_of_2(8), 8)
        self.assertEqual(highest_Power_of_2(16), 16)
        self.assertEqual(highest_Power_of_2(32), 32)

    def test_zero(self):
        self.assertEqual(highest_Power_of_2(0), 0)

    def test_negative_numbers(self):
        self.assertEqual(highest_Power_of_2(-1), 0)
        self.assertEqual(highest_Power_of_2(-2), 0)
        self.assertEqual(highest_Power_of_2(-4), 0)
        self.assertEqual(highest_Power_of_2(-8), 0)
        self.assertEqual(highest_Power_of_2(-16), 0)
        self.assertEqual(highest_Power_of_2(-32), 0)

    def test_large_numbers(self):
        self.assertEqual(highest_Power_of_2(2**64 - 1), 2**64 - 1)
        self.assertEqual(highest_Power_of_2(2**64), 2**64)

    def test_non_powers_of_2(self):
        self.assertEqual(highest_Power_of_2(3), 0)
        self.assertEqual(highest_Power_of_2(5), 0)
        self.assertEqual(highest_Power_of_2(7), 0)
        self.assertEqual(highest_Power_of_2(9), 0)
        self.assertEqual(highest_Power_of_2(11), 0)
