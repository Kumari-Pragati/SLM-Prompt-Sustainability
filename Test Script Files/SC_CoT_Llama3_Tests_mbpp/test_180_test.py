import unittest
from mbpp_180_code import distance_lat_long

class TestDistanceLatLong(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, 0), 0.0)

    def test_edge_cases(self):
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, 90), 3.14159265359)
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, -90), 3.14159265359)
        self.assertAlmostEqual(distance_lat_long(0, 0, 90, 0), 3.14159265359)
        self.assertAlmostEqual(distance_lat_long(0, 0, -90, 0), 3.14159265359)

    def test_boundary_cases(self):
        self.assertAlmostEqual(distance_lat_long(0, 0, 89, 0), 3.14159265359)
        self.assertAlmostEqual(distance_lat_long(0, 0, -89, 0), 3.14159265359)
        self.assertAlmostEqual(distance_lat_long(0, 0, 89, 90), 3.14159265359)
        self.assertAlmostEqual(distance_lat_long(0, 0, -89, 90), 3.14159265359)

    def test_special_cases(self):
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, 180), 3.14159265359)
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, 360), 0.0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            distance_lat_long('a', 0, 0, 0)
        with self.assertRaises(TypeError):
            distance_lat_long(0, 'a', 0, 0)
        with self.assertRaises(TypeError):
            distance_lat_long(0, 0, 'a', 0)
        with self.assertRaises(TypeError):
            distance_lat_long(0, 0, 0, 'a')
