import unittest
from mbpp_180_code import radians
from 180_code import distance_lat_long

class TestDistanceLatLong(unittest.TestCase):

    def test_normal_inputs(self):
        self.assertAlmostEqual(distance_lat_long(37.7749, -122.4194, 38.8951, -77.0363), 2489.447)
        self.assertAlmostEqual(distance_lat_long(-34.397, 150.644, -37.814, 145.167), 4000.0)

    def test_edge_and_boundary_conditions(self):
        self.assertAlmostEqual(distance_lat_long(90, 0, 90, 0), 0)
        self.assertAlmostEqual(distance_lat_long(-90, 0, -90, 0), 0)
        self.assertAlmostEqual(distance_lat_long(0, 180, 0, 180), 0)
        self.assertAlmostEqual(distance_lat_long(0, -180, 0, -180), 0)
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, 0), 0)

        self.assertAlmostEqual(distance_lat_long(90, 0, -90, 0), 6371.01 * acos(-1), places=7)
        self.assertAlmostEqual(distance_lat_long(-90, 0, 90, 0), 6371.01 * acos(-1), places=7)
        self.assertAlmostEqual(distance_lat_long(0, 180, 0, -180), 6371.01 * acos(-1), places=7)
        self.assertAlmostEqual(distance_lat_long(0, -180, 0, 180), 6371.01 * acos(-1), places=7)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            distance_lat_long(90, 181, 90, 0)
        with self.assertRaises(ValueError):
            distance_lat_long(-90, -181, -90, 0)
        with self.assertRaises(ValueError):
            distance_lat_long(0, 360, 0, 0)
        with self.assertRaises(ValueError):
            distance_lat_long(0, -360, 0, 0)
