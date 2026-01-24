import unittest
from mbpp_388_code import highest_Power_of_2

class TestHighestPowerOf2(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(highest_Power_of_2(0), 0)

    def test_one(self):
        self.assertEqual(highest_Power_of_2(1), 1)

    def test_two(self):
        self.assertEqual(highest_Power_of_2(2), 2)

    def test_three(self):
        self.assertEqual(highest_Power_of_2(3), 2)

    def test_four(self):
        self.assertEqual(highest_Power_of_2(4), 4)

    def test_five(self):
        self.assertEqual(highest_Power_of_2(5), 4)

    def test_negative_numbers(self):
        self.assertEqual(highest_Power_of_2(-1), 0)
        self.assertEqual(highest_Power_of_2(-2), 0)
        self.assertEqual(highest_Power_of_2(-3), 0)

    def test_large_numbers(self):
        self.assertEqual(highest_Power_of_2(1024), 1024)
        self.assertEqual(highest_Power_of_2(1025), 1024)
        self.assertEqual(highest_Power_of_2(1026), 1024)
        self.assertEqual(highest_Power_of_2(1027), 1024)
