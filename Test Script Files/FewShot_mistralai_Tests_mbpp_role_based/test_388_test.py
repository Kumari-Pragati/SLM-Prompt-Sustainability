import unittest
from mbpp_388_code import highest_Power_of_2

class TestHighestPowerOf2(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(highest_Power_of_2(8), 8)
        self.assertEqual(highest_Power_of_2(16), 16)
        self.assertEqual(highest_Power_of_2(256), 256)

    def test_zero(self):
        self.assertEqual(highest_Power_of_2(0), 0)

    def test_negative_numbers(self):
        self.assertEqual(highest_Power_of_2(-1), 0)
        self.assertEqual(highest_Power_of_2(-2), 0)
        self.assertEqual(highest_Power_of_2(-8), 0)

    def test_one(self):
        self.assertEqual(highest_Power_of_2(1), 1)

    def test_large_numbers(self):
        self.assertEqual(highest_Power_of_2(1024), 1024)
        self.assertEqual(highest_Power_of_2(16777216), 16777216)
