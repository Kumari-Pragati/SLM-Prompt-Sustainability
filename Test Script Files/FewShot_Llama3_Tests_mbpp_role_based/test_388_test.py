import unittest
from mbpp_388_code import highest_Power_of_2

class TestHighestPowerOf2(unittest.TestCase):
    def test_highest_power_of_2_positive(self):
        self.assertEqual(highest_Power_of_2(16), 16)

    def test_highest_power_of_2_negative(self):
        self.assertEqual(highest_Power_of_2(-16), 8)

    def test_highest_power_of_2_zero(self):
        self.assertEqual(highest_Power_of_2(0), 0)

    def test_highest_power_of_2_one(self):
        self.assertEqual(highest_Power_of_2(1), 1)

    def test_highest_power_of_2_large_number(self):
        self.assertEqual(highest_Power_of_2(1024), 1024)

    def test_highest_power_of_2_invalid_input(self):
        with self.assertRaises(TypeError):
            highest_Power_of_2("string")
