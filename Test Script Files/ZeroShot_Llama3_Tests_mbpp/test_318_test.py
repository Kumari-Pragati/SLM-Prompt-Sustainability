import unittest
from mbpp_318_code import max_volume

class TestMaxVolume(unittest.TestCase):

    def test_max_volume(self):
        self.assertEqual(max_volume(3), 6)
        self.assertEqual(max_volume(4), 24)
        self.assertEqual(max_volume(5), 60)
        self.assertEqual(max_volume(6), 120)
        self.assertEqual(max_volume(7), 210)
        self.assertEqual(max_volume(8), 336)
        self.assertEqual(max_volume(9), 504)
        self.assertEqual(max_volume(10), 720)

    def test_max_volume_edge_cases(self):
        self.assertEqual(max_volume(1), 0)
        self.assertEqual(max_volume(2), 2)
