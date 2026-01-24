import unittest
from mbpp_180_code import distance_lat_long

class TestDistanceLatLong(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(distance_lat_long(30, 30, 45, 45), 1571.514894471479)

    def test_edge_case_same_location(self):
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, 0), 0)

    def test_boundary_case_poles(self):
        self.assertAlmostEqual(distance_lat_long(90, 0, -90, 0), 20015.11517757818)

    def test_boundary_case_equator(self):
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, 180), 0)

    def test_corner_case_opposite_hemispheres(self):
        self.assertAlmostEqual(distance_lat_long(90, 0, -90, 180), 20037.51517757818)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            distance_lat_long(100, 0, 0, 0)
