import unittest
from mbpp_180_code import distance_lat_long

class TestDistanceLatLong(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(distance_lat_long(37.7749, -122.4194, 38.3219, -77.0369), 2489.945)
        self.assertAlmostEqual(distance_lat_long(-34.397, -58.377, -34.609, -58.367), 12.76)

    def test_edge_case_lat(self):
        self.assertAlmostEqual(distance_lat_long(90, 0, 89.9999, 0), 6371.01)
        self.assertAlmostEqual(distance_lat_long(-90, 0, -89.9999, 0), 6371.01)

    def test_edge_case_lon(self):
        self.assertAlmostEqual(distance_lat_long(37.7749, 180, 38.3219, 179.9999), 6371.01)
        self.assertAlmostEqual(distance_lat_long(37.7749, -180, 38.3219, -179.9999), 6371.01)

    def test_invalid_input(self):
        self.assertRaises(ValueError, distance_lat_long, 90, 181, 89, 180)
        self.assertRaises(ValueError, distance_lat_long, -90, -181, -89, -180)
