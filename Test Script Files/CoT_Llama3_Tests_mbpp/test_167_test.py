import unittest
from mbpp_167_code import next_Power_Of_2

class TestNextPowerOf2(unittest.TestCase):

    def test_power_of_2(self):
        self.assertEqual(next_Power_Of_2(8), 8)

    def test_next_power_of_2(self):
        self.assertEqual(next_Power_Of_2(7), 8)

    def test_power_of_1(self):
        self.assertEqual(next_Power_Of_2(1), 1)

    def test_power_of_0(self):
        self.assertEqual(next_Power_Of_2(0), 1)

    def test_negative_number(self):
        with self.assertRaises(TypeError):
            next_Power_Of_2(-1)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            next_Power_Of_2(3.5)
