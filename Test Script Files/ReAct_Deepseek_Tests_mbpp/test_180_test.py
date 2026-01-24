import unittest
from mbpp_180_code import distance_lat_long

class TestDistanceLatLong(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, 0), 0)

    def test_boundary_case_same_location(self):
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, 0), 0)

    def test_boundary_case_antipodes(self):
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, 180), 20015.115534)

    def test_typical_case_close_distance(self):
        self.assertAlmostEqual(distance_lat_long(30, 30, 30, 30), 0)

    def test_typical_case_far_distance(self):
        self.assertAlmostEqual(distance_lat_long(0, 0, 90, 180), 20015.115534)

    def test_edge_case_negative_latitude(self):
        self.assertAlmostEqual(distance_lat_long(-30, 30, 30, 30), 0)

    def test_edge_case_latitude_greater_than_90(self):
        with self.assertRaises(ValueError):
            distance_lat_long(91, 0, 0, 0)

    def test_edge_case_longitude_greater_than_180(self):
        with self.assertRaises(ValueError):
            distance_lat_long(0, 181, 0, 0)
