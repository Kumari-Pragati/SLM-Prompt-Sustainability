import unittest
from mbpp_167_code import next_Power_Of_2

class TestNextPowerOf2(unittest.TestCase):
    def test_power_of_2(self):
        self.assertEqual(next_Power_Of_2(4), 8)
        self.assertEqual(next_Power_Of_2(8), 16)
        self.assertEqual(next_Power_Of_2(16), 32)

    def test_non_power_of_2(self):
        self.assertEqual(next_Power_Of_2(3), 4)
        self.assertEqual(next_Power_Of_2(5), 8)
        self.assertEqual(next_Power_Of_2(7), 8)

    def test_zero(self):
        self.assertEqual(next_Power_Of_2(0), 1)

    def test_negative_numbers(self):
        self.assertEqual(next_Power_Of_2(-1), 1)
        self.assertEqual(next_Power_Of_2(-2), 1)
        self.assertEqual(next_Power_Of_2(-3), 4)
