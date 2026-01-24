import unittest
from mbpp_199_code import highest_Power_of_2

class TestHighestPowerOf2(unittest.TestCase):
    def test_highest_power_of_2_positive_numbers(self):
        self.assertEqual(highest_Power_of_2(16), 16)
        self.assertEqual(highest_Power_of_2(32), 32)
        self.assertEqual(highest_Power_of_2(64), 64)

    def test_highest_power_of_2_zero(self):
        self.assertEqual(highest_Power_of_2(0), 0)

    def test_highest_power_of_2_negative_numbers(self):
        self.assertEqual(highest_Power_of_2(-16), 0)
        self.assertEqual(highest_Power_of_2(-32), 0)
        self.assertEqual(highest_Power_of_2(-64), 0)

    def test_highest_power_of_2_non_integer_numbers(self):
        with self.assertRaises(TypeError):
            highest_Power_of_2(3.14)
