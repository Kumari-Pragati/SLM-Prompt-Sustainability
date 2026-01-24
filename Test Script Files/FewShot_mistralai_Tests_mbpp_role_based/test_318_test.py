import unittest
from mbpp_318_code import max_volume

class TestMaxVolume(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(max_volume(3), 6)
        self.assertEqual(max_volume(4), 12)
        self.assertEqual(max_volume(5), 24)

    def test_zero(self):
        self.assertEqual(max_volume(0), 0)

    def test_negative_integer(self):
        self.assertEqual(max_volume(-1), 0)
        self.assertEqual(max_volume(-2), 0)
        self.assertEqual(max_volume(-3), 0)

    def test_large_integer(self):
        self.assertEqual(max_volume(100), 66450)
        self.assertEqual(max_volume(1000), 249999999)
        self.assertEqual(max_volume(10000), 10000000000)
