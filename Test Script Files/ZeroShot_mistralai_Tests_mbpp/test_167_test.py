import unittest
from mbpp_167_code import next_Power_Of_2

class TestNextPowerOf2(unittest.TestCase):

    def test_next_power_of_2_positive(self):
        self.assertEqual(next_Power_Of_2(1), 2)
        self.assertEqual(next_Power_Of_2(2), 4)
        self.assertEqual(next_Power_Of_2(4), 8)
        self.assertEqual(next_Power_Of_2(8), 16)
        self.assertEqual(next_Power_Of_2(16), 32)
        self.assertEqual(next_Power_Of_2(32), 64)
        self.assertEqual(next_Power_Of_2(64), 128)
        self.assertEqual(next_Power_Of_2(128), 256)
        self.assertEqual(next_Power_Of_2(256), 512)
        self.assertEqual(next_Power_Of_2(512), 1024)
        self.assertEqual(next_Power_Of_2(1024), 2048)

    def test_next_power_of_2_zero(self):
        self.assertEqual(next_Power_Of_2(0), 1)

    def test_next_power_of_2_negative(self):
        self.assertEqual(next_Power_Of_2(-1), 1)
        self.assertEqual(next_Power_Of_2(-2), 1)
        self.assertEqual(next_Power_Of_2(-4), 4)
        self.assertEqual(next_Power_Of_2(-8), 8)
        self.assertEqual(next_Power_Of_2(-16), 16)
        self.assertEqual(next_Power_Of_2(-32), 32)
        self.assertEqual(next_Power_Of_2(-64), 64)
        self.assertEqual(next_Power_Of_2(-128), 128)
        self.assertEqual(next_Power_Of_2(-256), 256)
        self.assertEqual(next_Power_Of_2(-512), 512)
        self.assertEqual(next_Power_Of_2(-1024), 1024)

    def test_next_power_of_2_one(self):
        self.assertEqual(next_Power_Of_2(1), 2)

    def test_next_power_of_2_odd(self):
        self.assertEqual(next_Power_Of_2(3), 8)
        self.assertEqual(next_Power_Of_2(5), 32)
        self.assertEqual(next_Power_Of_2(7), 64)
        self.assertEqual(next_Power_Of_2(9), 128)
        self.assertEqual(next_Power_Of_2(11), 256)
        self.assertEqual(next_Power_Of_2(13), 512)
        self.assertEqual(next_Power_Of_2(15), 1024)
        self.assertEqual(next_Power_Of_2(17), 2048)
        self.assertEqual(next_Power_Of_2(19), 4096)
        self.assertEqual(next_Power_Of_2(21), 8192)
        self.assertEqual(next_Power_Of_2(23), 16384)
