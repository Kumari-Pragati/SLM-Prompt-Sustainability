import unittest
from mbpp_318_code import max_volume

class TestMaxVolume(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(max_volume(3), 6)
        self.assertEqual(max_volume(4), 24)
        self.assertEqual(max_volume(5), 100)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(max_volume(0), 0)
        self.assertEqual(max_volume(1), 1)
        self.assertEqual(max_volume(2), 8)

    def test_negative_input(self):
        self.assertRaises(ValueError, max_volume, -1)
        self.assertRaises(ValueError, max_volume, -2)
