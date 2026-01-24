import unittest
from mbpp_167_code import next_Power_Of_2

class TestNextPowerOf2(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(next_Power_Of_2(1), 1)
        self.assertEqual(next_Power_Of_2(2), 2)
        self.assertEqual(next_Power_Of_2(4), 4)
        self.assertEqual(next_Power_Of_2(8), 8)
        self.assertEqual(next_Power_Of_2(16), 16)
        self.assertEqual(next_Power_Of_2(32), 32)
        self.assertEqual(next_Power_Of_2(64), 64)
        self.assertEqual(next_Power_Of_2(128), 128)
        self.assertEqual(next_Power_Of_2(256), 256)
        self.assertEqual(next_Power_Of_2(512), 512)
        self.assertEqual(next_Power_Of_2(1024), 1024)

    def test_zero(self):
        self.assertEqual(next_Power_Of_2(0), 1)

    def test_negative_numbers(self):
        self.assertEqual(next_Power_Of_2(-1), 1)
        self.assertEqual(next_Power_Of_2(-2), 1)
        self.assertEqual(next_Power_Of_2(-3), 1)
        self.assertEqual(next_Power_Of_2(-4), 1)
        self.assertEqual(next_Power_Of_2(-5), 1)
        self.assertEqual(next_Power_Of_2(-6), 1)
        self.assertEqual(next_Power_Of_2(-7), 1)
        self.assertEqual(next_Power_Of_2(-8), 1)
        self.assertEqual(next_Power_Of_2(-9), 1)
        self.assertEqual(next_Power_Of_2(-10), 1)
        self.assertEqual(next_Power_Of_2(-11), 1)
        self.assertEqual(next_Power_Of_2(-12), 1)
        self.assertEqual(next_Power_Of_2(-13), 1)
        self.assertEqual(next_Power_Of_2(-14), 1)
        self.assertEqual(next_Power_Of_2(-15), 1)
        self.assertEqual(next_Power_Of_2(-16), 1)
        self.assertEqual(next_Power_Of_2(-255), 256)
        self.assertEqual(next_Power_Of_2(-256), 512)
        self.assertEqual(next_Power_Of_2(-511), 1024)
        self.assertEqual(next_Power_Of_2(-512), 1024)
        self.assertEqual(next_Power_Of_2(-1023), 2048)
        self.assertEqual(next_Power_Of_2(-1024), 2048)
        self.assertEqual(next_Power_Of_2(-2047), 4096)
        self.assertEqual(next_Power_Of_2(-2048), 4096)
        self.assertEqual(next_Power_Of_2(-4095), 8192)
        self.assertEqual(next_Power_Of_2(-4096), 8192)
        self.assertEqual(next_Power_Of_2(-8191), 16384)
        self.assertEqual(next_Power_Of_2(-8192), 16384)
        self.assertEqual(next_Power_Of_2(-16383), 32768)
        self.assertEqual(next_Power_Of_2(-16384), 32768)

    def test_one(self):
        self.assertEqual(next_Power_Of_2(1), 1)

    def test_invalid_inputs