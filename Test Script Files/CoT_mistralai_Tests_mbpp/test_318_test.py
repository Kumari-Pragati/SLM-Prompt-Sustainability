import unittest
from mbpp_318_code import max_volume

class TestMaxVolume(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(max_volume(3), 6)
        self.assertEqual(max_volume(4), 24)
        self.assertEqual(max_volume(5), 100)

    def test_edge_input(self):
        self.assertEqual(max_volume(1), 1)
        self.assertEqual(max_volume(2), 8)
        self.assertEqual(max_volume(6), 288)

    def test_boundary_input(self):
        self.assertEqual(max_volume(0), 0)
        self.assertEqual(max_volume(1000), 664579500)

    def test_invalid_input(self):
        self.assertRaises(ValueError, max_volume, -1)
        self.assertRaises(ValueError, max_volume, float('inf'))
