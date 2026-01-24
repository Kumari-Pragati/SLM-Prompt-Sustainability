import unittest
from mbpp_180_code import distance_lat_long

class TestDistanceLatLong(unittest.TestCase):
    def test_typical_use_case(self):
        slat = radians(40.7128)
        slon = radians(-74.0060)
        elat = radians(34.0522)
        elon = radians(-118.2437)
        self.assertAlmostEqual(distance_lat_long(slat, slon, elat, elon), 4.6659, places=4)

    def test_edge_case_zero(self):
        slat = radians(0)
        slon = radians(0)
        elat = radians(0)
        elon = radians(0)
        self.assertAlmostEqual(distance_lat_long(slat, slon, elat, elon), 0, places=4)

    def test_edge_case_pi(self):
        slat = radians(90)
        slon = radians(90)
        elat = radians(0)
        elon = radians(0)
        self.assertAlmostEqual(distance_lat_long(slat, slon, elat, elon), 3.1416, places=4)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            distance_lat_long("40.7128", radians(-74.0060), "34.0522", radians(-118.2437))
