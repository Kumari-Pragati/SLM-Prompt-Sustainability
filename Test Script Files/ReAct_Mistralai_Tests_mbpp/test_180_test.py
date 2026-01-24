import unittest
from mbpp_180_code import distance_lat_long

class TestDistanceLatLong(unittest.TestCase):

    def test_positive_values(self):
        # Typical case: positive latitude and longitude values
        self.assertAlmostEqual(distance_lat_long(37.7749, -122.4194, 38.7345, -77.0459), 2491.111, delta=1)

    def test_zero_values(self):
        # Edge case: zero latitude or longitude values
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, 0), 0, delta=0)
        self.assertAlmostEqual(distance_lat_long(37.7749, 0, 38.7345, 0), 2491.111, delta=1)
        self.assertAlmostEqual(distance_lat_long(0, -122.4194, 0, -77.0459), 2491.111, delta=1)

    def test_negative_values(self):
        # Typical case: negative latitude and longitude values
        self.assertAlmostEqual(distance_lat_long(-37.7749, 122.4194, -38.7345, 77.0459), 2491.111, delta=1)

    def test_large_values(self):
        # Edge case: large latitude and longitude values
        self.assertAlmostEqual(distance_lat_long(90, 180, 90, 180), 0, delta=0)
        self.assertAlmostEqual(distance_lat_long(-90, -180, -90, -180), 0, delta=0)

    def test_invalid_input(self):
        # Error case: invalid input (non-numeric or out-of-range values)
        self.assertRaises(ValueError, distance_lat_long, 'not_number', 37.7749, -122.4194)
        self.assertRaises(ValueError, distance_lat_long, 37.7749, 'not_number', -122.4194)
        self.assertRaises(ValueError, distance_lat_long, 37.7749, -122.4194, 'not_number')
        self.assertRaises(ValueError, distance_lat_long, -90.01, -180, 90, 180)
        self.assertRaises(ValueError, distance_lat_long, 90, 180.01, 90, 180)
