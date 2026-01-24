import unittest
from mbpp_180_code import radians
from 180_code import distance_lat_long

class TestDistanceLatLong(unittest.TestCase):

    def test_distance_lat_long(self):
        self.assertAlmostEqual(distance_lat_long(37.7749, -122.4194, 38.3834, -77.0459), 2490.8325)
        self.assertAlmostEqual(distance_lat_long(51.5074, -0.1278, 51.5458, -0.0735), 1.6094)
        self.assertAlmostEqual(distance_lat_long(25.0000, 121.0000, 26.0000, 122.0000), 6371.01)
        self.assertAlmostEqual(distance_lat_long(90, 0, 90, 180), 6371.01)
        self.assertRaises(ValueError, distance_lat_long, -91, 0, 91, 0)
        self.assertRaises(ValueError, distance_lat_long, 91, 181, 91, 0)
        self.assertRaises(ValueError, distance_lat_long, 90, -181, 90, 0)
        self.assertRaises(ValueError, distance_lat_long, 90, 0, -91, 0)
