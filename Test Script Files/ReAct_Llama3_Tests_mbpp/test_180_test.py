import unittest
from mbpp_180_code import distance_lat_long

class TestDistanceLatLong(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, 0), 0, places=5)

    def test_edge_case_zero_lat(self):
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, 90), 6371.01, places=5)

    def test_edge_case_zero_lon(self):
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, 0), 6371.01, places=5)

    def test_edge_case_max_lat(self):
        self.assertAlmostEqual(distance_lat_long(90, 0, 90, 0), 0, places=5)

    def test_edge_case_max_lon(self):
        self.assertAlmostEqual(distance_lat_long(0, 90, 0, 90), 0, places=5)

    def test_edge_case_max_lat_max_lon(self):
        self.assertAlmostEqual(distance_lat_long(90, 90, 90, 90), 0, places=5)

    def test_edge_case_max_lat_min_lon(self):
        self.assertAlmostEqual(distance_lat_long(90, -90, 90, -90), 0, places=5)

    def test_edge_case_min_lat_max_lon(self):
        self.assertAlmostEqual(distance_lat_long(-90, 90, -90, 90), 0, places=5)

    def test_edge_case_min_lat_min_lon(self):
        self.assertAlmostEqual(distance_lat_long(-90, -90, -90, -90), 0, places=5)

    def test_edge_case_min_lat_max_lon(self):
        self.assertAlmostEqual(distance_lat_long(-90, 90, -90, 90), 0, places=5)

    def test_edge_case_max_lat_min_lon(self):
        self.assertAlmostEqual(distance_lat_long(90, -90, 90, -90), 0, places=5)

    def test_edge_case_min_lat_zero_lon(self):
        self.assertAlmostEqual(distance_lat_long(-90, 0, -90, 0), 6371.01, places=5)

    def test_edge_case_max_lat_zero_lon(self):
        self.assertAlmostEqual(distance_lat_long(90, 0, 90, 0), 6371.01, places=5)

    def test_edge_case_min_lat_max_lon(self):
        self.assertAlmostEqual(distance_lat_long(-90, 90, -90, 90), 0, places=5)

    def test_edge_case_max_lat_max_lon(self):
        self.assertAlmostEqual(distance_lat_long(90, 90, 90, 90), 0, places=5)

    def test_edge_case_min_lat_min_lon(self):
        self.assertAlmostEqual(distance_lat_long(-90, -90, -90, -90), 0, places=5)

    def test_edge_case_max_lat_min_lon(self):
        self.assertAlmostEqual(distance_lat_long(90, -90, 90, -90), 0, places=5)

    def test_edge_case_min_lat_zero_lon(self):
        self.assertAlmostEqual(distance_lat_long(-90, 0, -90, 0), 6371.01, places=5)

    def test_edge_case_max_lat_zero_lon(self):
        self.assertAlmostEqual(distance_lat_long(90, 0, 90, 0), 6371.01, places=5)

    def test_edge_case_min_lat_max_lon(self):
        self.assertAlmostEqual(distance_lat_long(-90, 90, -90, 90), 0, places=5)

    def test_edge_case_max_lat_max_lon(self):
        self.assertAlmostEqual(distance_lat_long(90, 90, 90, 90), 0, places=5)

    def test_edge_case_min_lat_min_lon(self):
        self.assertAlmostEqual(distance_lat_long(-90, -90, -90, -90), 0, places=5)

    def test_edge_case_max_lat_min_lon(self):
        self.assertAlmostEqual(distance_lat_long(90, -90, 90, -90), 0, places=5)
