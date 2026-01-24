import unittest
from mbpp_199_code import highest_Power_of_2

class TestHighestPowerOf2(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(highest_Power_of_2(0), 0)
        self.assertEqual(highest_Power_of_2(1), 1)
        self.assertEqual(highest_Power_of_2(2), 2)
        self.assertEqual(highest_Power_of_2(3), 2)
        self.assertEqual(highest_Power_of_2(4), 4)
        self.assertEqual(highest_Power_of_2(5), 4)
        self.assertEqual(highest_Power_of_2(6), 4)
        self.assertEqual(highest_Power_of_2(7), 4)
        self.assertEqual(highest_Power_of_2(8), 8)
        self.assertEqual(highest_Power_of_2(9), 8)
        self.assertEqual(highest_Power_of_2(10), 8)

    def test_edge(self):
        self.assertEqual(highest_Power_of_2(15), 8)
        self.assertEqual(highest_Power_of_2(16), 16)
        self.assertEqual(highest_Power_of_2(32), 32)
        self.assertEqual(highest_Power_of_2(64), 64)
        self.assertEqual(highest_Power_of_2(128), 128)
        self.assertEqual(highest_Power_of_2(255), 128)
        self.assertEqual(highest_Power_of_2(256), 256)
        self.assertEqual(highest_Power_of_2(512), 256)
        self.assertEqual(highest_Power_of_2(1024), 512)
        self.assertEqual(highest_Power_of_2(2048), 1024)

    def test_complex(self):
        self.assertEqual(highest_Power_of_2(2049), 1024)
        self.assertEqual(highest_Power_of_2(2050), 1024)
        self.assertEqual(highest_Power_of_2(2048), 1024)
        self.assertEqual(highest_Power_of_2(2047), 1024)
        self.assertEqual(highest_Power_of_2(2046), 1024)
