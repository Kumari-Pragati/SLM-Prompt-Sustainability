import unittest
from mbpp_318_code import max_volume

class TestMaxVolume(unittest.TestCase):

    def test_max_volume_zero(self):
        self.assertEqual(max_volume(0), 0)

    def test_max_volume_one(self):
        self.assertEqual(max_volume(1), 1)

    def test_max_volume_small(self):
        self.assertEqual(max_volume(3), 6)

    def test_max_volume_medium(self):
        self.assertEqual(max_volume(10), 288)

    def test_max_volume_large(self):
        self.assertEqual(max_volume(100), 664500)
