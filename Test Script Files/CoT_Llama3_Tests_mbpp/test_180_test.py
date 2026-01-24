import unittest
from mbpp_180_code import distance_lat_long

class TestDistanceLatLong(unittest.TestCase):

    def test_distance_lat_long_typical(self):
        self.assertAlmostEqual(distance_lat_long(0, 0, 1, 1), 111.32, places=2)

    def test_distance_lat_long_edge(self):
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, 0), 0.0, places=2)

    def test_distance_lat_long_invalid_input(self):
        with self.assertRaises(TypeError):
            distance_lat_long('a', 'b', 'c', 'd')

    def test_distance_lat_long_invalid_input2(self):
        with self.assertRaises(TypeError):
            distance_lat_long(0, 0, 'a', 'b')

    def test_distance_lat_long_invalid_input3(self):
        with self.assertRaises(TypeError):
            distance_lat_long(0, 0, 0, 'a')

    def test_distance_lat_long_invalid_input4(self):
        with self.assertRaises(TypeError):
            distance_lat_long('a', 'b', 'c', 'd')

    def test_distance_lat_long_invalid_input5(self):
        with self.assertRaises(TypeError):
            distance_lat_long(0, 0, 0, 0)
