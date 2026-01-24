import unittest
from mbpp_180_code import distance_lat_long

class TestDistanceLatLong(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, 0), 0, places=2)

    def test_typical_case_2(self):
        self.assertAlmostEqual(distance_lat_long(30, 30, 30, 30), 0, places=2)

    def test_edge_case_same_coordinates(self):
        self.assertAlmostEqual(distance_lat_long(90, 0, 90, 0), 0, places=2)

    def test_edge_case_opposite_coordinates(self):
        self.assertAlmostEqual(distance_lat_long(90, 0, -90, 0), 20015.11678654755, places=2)

    def test_invalid_input_latitude_out_of_range(self):
        with self.assertRaises(ValueError):
            distance_lat_long(180, 0, 0, 0)

    def test_invalid_input_longitude_out_of_range(self):
        with self.assertRaises(ValueError):
            distance_lat_long(0, 180, 0, 0)

    def test_invalid_input_latitude_not_a_number(self):
        with self.assertRaises(TypeError):
            distance_lat_long('a', 0, 0, 0)

    def test_invalid_input_longitude_not_a_number(self):
        with self.assertRaises(TypeError):
            distance_lat_long(0, 'b', 0, 0)
