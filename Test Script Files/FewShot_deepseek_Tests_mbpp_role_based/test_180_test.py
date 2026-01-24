import unittest
from mbpp_180_code import distance_lat_long

class TestDistanceLatLong(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, 0), 0)

    def test_boundary_conditions(self):
        self.assertAlmostEqual(distance_lat_long(0, 0, 90, 0), 6371.01)
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, 180), 6371.01 * 2)

    def test_edge_cases(self):
        self.assertAlmostEqual(distance_lat_long(0, 0, 90, 90), 6371.01 * 2**0.5)
        self.assertAlmostEqual(distance_lat_long(0, 0, -90, 0), 6371.01)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            distance_lat_long(91, 0, 0, 0)
        with self.assertRaises(ValueError):
            distance_lat_long(-91, 0, 0, 0)
        with self.assertRaises(ValueError):
            distance_lat_long(0, 181, 0, 0)
        with self.assertRaises(ValueError):
            distance_lat_long(0, -181, 0, 0)
