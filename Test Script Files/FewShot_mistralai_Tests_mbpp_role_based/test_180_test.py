import unittest
from mbpp_180_code import distance_lat_long

class TestDistanceLatLong(unittest.TestCase):
    def test_positive_values(self):
        self.assertAlmostEqual(distance_lat_long(37.7749, -122.4194, 38.7283, -77.0462), 2491.28)
        self.assertAlmostEqual(distance_lat_long(51.5074, -0.1278, 52.5200, 1.1238), 87.44)

    def test_zero_values(self):
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, 0), 0)

    def test_negative_values(self):
        self.assertAlmostEqual(distance_lat_long(-90, -180, -90, 180), 6371.01)
        self.assertAlmostEqual(distance_lat_long(-90, 180, -90, -180), 6371.01)

    def test_invalid_input(self):
        self.assertRaises(ValueError, distance_lat_long, -91, -181, 90, 180)
        self.assertRaises(ValueError, distance_lat_long, 91, 181, -90, -180)
