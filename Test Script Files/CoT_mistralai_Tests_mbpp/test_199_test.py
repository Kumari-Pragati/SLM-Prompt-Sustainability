import unittest
from199_code import highest_Power_of_2

class TestHighestPowerOf2(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(highest_Power_of_2(0), 0)
        self.assertEqual(highest_Power_of_2(1), 1)
        self.assertEqual(highest_Power_of_2(2), 2)
        self.assertEqual(highest_Power_of_2(3), 2)
        self.assertEqual(highest_Power_of_2(4), 4)
        self.assertEqual(highest_Power_of_2(5), 4)
        self.assertEqual(highest_Power_of_2(6), 6)
        self.assertEqual(highest_Power_of_2(7), 4)
        self.assertEqual(highest_Power_of_2(8), 8)
        self.assertEqual(highest_Power_of_2(9), 8)
        self.assertEqual(highest_Power_of_2(10), 10)
        self.assertEqual(highest_Power_of_2(11), 8)
        self.assertEqual(highest_Power_of_2(12), 12)
        self.assertEqual(highest_Power_of_2(13), 8)
        self.assertEqual(highest_Power_of_2(14), 14)
        self.assertEqual(highest_Power_of_2(15), 16)
        self.assertEqual(highest_Power_of_2(16), 16)
        self.assertEqual(highest_Power_of_2(17), 16)
        self.assertEqual(highest_Power_of_2(18), 18)
        self.assertEqual(highest_Power_of_2(19), 18)
        self.assertEqual(highest_Power_of_2(20), 20)
        self.assertEqual(highest_Power_of_2(21), 20)
        self.assertEqual(highest_Power_of_2(22), 22)
        self.assertEqual(highest_Power_of_2(23), 20)
        self.assertEqual(highest_Power_of_2(24), 24)
        self.assertEqual(highest_Power_of_2(25), 24)
        self.assertEqual(highest_Power_of_2(26), 26)
        self.assertEqual(highest_Power_of_2(27), 24)
        self.assertEqual(highest_Power_of_2(28), 28)
        self.assertEqual(highest_Power_of_2(29), 28)
        self.assertEqual(highest_Power_of_2(30), 30)
        self.assertEqual(highest_Power_of_2(31), 30)

    def test_zero(self):
        self.assertEqual(highest_Power_of_2(0), 0)

    def test_negative_numbers(self):
        self.assertEqual(highest_Power_of_2(-1), 0)
        self.assertEqual(highest_Power_of_2(-2), 0)
        self.assertEqual(highest_Power_of_2(-3), 0)
        self.assertEqual(highest_Power_of_2(-4), 0)
        self.assertEqual(highest_Power_of_2(-5), 0)
        self.assertEqual(highest_Power_of_2(-6), 0)
        self.assertEqual(highest_Power_of_2(-7), 0)
        self.assertEqual(highest_Power_of_2(-8), 0)
        self.assertEqual(highest_Power_of_2(-9), 0)
        self.assertEqual(highest_Power_of_2(-10), 0)
        self.assertEqual