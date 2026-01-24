import unittest
from mbpp_180_code import distance_lat_long

class TestDistanceLatLong(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, 0), 0)
        self.assertAlmostEqual(distance_lat_long(30, 30, 30, 30), 0)

    def test_edge_conditions(self):
        self.assertAlmostEqual(distance_lat_long(0, 0, 90, 0), 20015100.0)
        self.assertAlmostEqual(distance_lat_long(0, 0, -90, 0), 20015100.0)
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, 180), 20037508.34)
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, -180), 20037508.34)

    def test_complex_cases(self):
        self.assertAlmostEqual(distance_lat_long(37.7749, -122.4194, 51.5074, -0.1278), 5575.88)
        self.assertAlmostEqual(distance_lat_long(40.7128, 74.0060, 34.0522, -118.2437), 3857.43)
