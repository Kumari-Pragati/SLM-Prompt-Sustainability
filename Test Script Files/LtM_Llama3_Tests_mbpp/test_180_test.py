import unittest
from mbpp_180_code import distance_lat_long

class TestDistanceLatLong(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, 0), 0, places=5)
        self.assertAlmostEqual(distance_lat_long(0, 0, 45, 45), 6371.01, places=5)
        self.assertAlmostEqual(distance_lat_long(0, 0, 90, 90), 6371.01, places=5)

    def test_edge_cases(self):
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, 180), 6371.01, places=5)
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, 360), 0, places=5)
        self.assertAlmostEqual(distance_lat_long(0, 0, 90, 0), 6371.01, places=5)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            distance_lat_long('a', 0, 0, 0)
        with self.assertRaises(TypeError):
            distance_lat_long(0, 'a', 0, 0)
        with self.assertRaises(TypeError):
            distance_lat_long(0, 0, 'a', 0)
        with self.assertRaises(TypeError):
            distance_lat_long(0, 0, 0, 'a')
