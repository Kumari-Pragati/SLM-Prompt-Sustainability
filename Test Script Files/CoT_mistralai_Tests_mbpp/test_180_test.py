import unittest
from mbpp_180_code import radians, sin, cos, acos
from 180_code import distance_lat_long

class TestDistanceLatLong(unittest.TestCase):

    def test_positive_values(self):
        self.assertAlmostEqual(distance_lat_long(37.7749, -122.4194, 38.7398, -77.0369), 2491.474)
        self.assertAlmostEqual(distance_lat_long(51.5074, -0.1278, 52.5200, 1.1278), 87.572)
        self.assertAlmostEqual(distance_lat_long(-34.397, -58.3737, -34.609, -58.3613), 11.181)

    def test_negative_values(self):
        self.assertAlmostEqual(distance_lat_long(-37.7749, 122.4194, -38.7398, 177.0369), 2491.474)
        self.assertAlmostEqual(distance_lat_long(-51.5074, 180.1278, -52.5200, -181.1278), 87.572)
        self.assertAlmostEqual(distance_lat_long(34.397, -360.3737, 34.609, -360.3613), 11.181)

    def test_zero_values(self):
        self.assertEqual(distance_lat_long(0, 0, 0, 0), 0)
        self.assertEqual(distance_lat_long(0, 360, 0, 0), 0)
        self.assertEqual(distance_lat_long(0, 0, 0, 360), 0)

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, distance_lat_long, -91, 180, 91, 180)
        self.assertRaises(ValueError, distance_lat_long, 91, -180, 91, -180)
        self.assertRaises(ValueError, distance_lat_long, 90, 0, 90, 360)
        self.assertRaises(ValueError, distance_lat_long, 90, 360, 90, 0)
