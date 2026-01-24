import unittest
from mbpp_180_code import distance_lat_long

class TestDistanceLatLong(unittest.TestCase):

    def test_simple(self):
        self.assertAlmostEqual(distance_lat_long(37.7749, -122.4194, 38.7398, -77.0369), 2490.7121)
        self.assertAlmostEqual(distance_lat_long(-37.7749, 122.4194, -38.7398, 77.0369), 2490.7121)

    def test_edge_and_boundary(self):
        self.assertAlmostEqual(distance_lat_long(90, 0, 90, 0), 0)
        self.assertAlmostEqual(distance_lat_long(-90, 0, -90, 0), 0)
        self.assertAlmostEqual(distance_lat_long(0, 180, 0, 180), 0)
        self.assertAlmostEqual(distance_lat_long(0, -180, 0, -180), 0)
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, 0), 0)

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, distance_lat_long, -100, 180, 100, -180)
        self.assertRaises(ValueError, distance_lat_long, 100, -180, 100, 180)
        self.assertRaises(ValueError, distance_lat_long, 90, 0, -90, 0)
        self.assertRaises(ValueError, distance_lat_long, -90, 0, 90, 0)
        self.assertRaises(ValueError, distance_lat_long, 0, 180, 0, -180)
        self.assertRaises(ValueError, distance_lat_long, 0, -180, 0, 180)
