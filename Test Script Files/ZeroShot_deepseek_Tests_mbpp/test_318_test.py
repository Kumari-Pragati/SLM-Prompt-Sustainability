import unittest
from mbpp_318_code import max_volume

class TestMaxVolume(unittest.TestCase):

    def test_max_volume(self):
        self.assertEqual(max_volume(1), 0)
        self.assertEqual(max_volume(2), 0)
        self.assertEqual(max_volume(3), 0)
        self.assertEqual(max_volume(4), 6)
        self.assertEqual(max_volume(5), 12)
        self.assertEqual(max_volume(6), 24)
        self.assertEqual(max_volume(7), 32)
        self.assertEqual(max_volume(8), 48)
        self.assertEqual(max_volume(9), 72)
        self.assertEqual(max_volume(10), 90)
