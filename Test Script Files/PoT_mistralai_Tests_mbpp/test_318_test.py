import unittest
from mbpp_318_code import max_volume

class TestMaxVolume(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(max_volume(3), 6)
        self.assertEqual(max_volume(4), 24)
        self.assertEqual(max_volume(5), 100)

    def test_edge_case(self):
        self.assertEqual(max_volume(1), 1)
        self.assertEqual(max_volume(2), 8)

    def test_boundary_case(self):
        self.assertEqual(max_volume(0), 0)
        self.assertEqual(max_volume(1000), 6494000000)
