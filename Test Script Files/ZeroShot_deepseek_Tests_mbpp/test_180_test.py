import unittest
from mbpp_180_code import radians, sin, cos, acos
from mbpp_180_code import distance_lat_long

class TestDistanceLatLong(unittest.TestCase):
    def test_distance_lat_long(self):
        # Test case 1: Same coordinates
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, 0), 0)

        # Test case 2: Coordinates at the equator
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, 180), 20015.11530234763)

        # Test case 3: Coordinates at the same longitude but different latitudes
        self.assertAlmostEqual(distance_lat_long(0, 0, 90, 0), 20015.11530234763)

        # Test case 4: Coordinates at the same latitude but different longitudes
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, 90), 10007.557651173815)

        # Test case 5: Coordinates at the poles
        self.assertAlmostEqual(distance_lat_long(90, 0, -90, 0), 20015.11530234763)

        # Test case 6: Coordinates at the same longitude but different latitudes
        self.assertAlmostEqual(distance_lat_long(0, 0, -90, 0), 20015.11530234763)

        # Test case 7: Coordinates at the same latitude but different longitudes
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, -90), 10007.557651173815)

        # Test case 8: Coordinates at the poles
        self.assertAlmostEqual(distance_lat_long(-90, 0, 90, 0), 20015.11530234763)

        # Test case 9: Coordinates at the same longitude but different latitudes
        self.assertAlmostEqual(distance_lat_long(-90, 0, 0, 0), 20015.11530234763)

        # Test case 10: Coordinates at the same latitude but different longitudes
        self.assertAlmostEqual(distance_lat_long(0, -90, 0, 90), 20015.11530234763)

        # Test case 11: Coordinates at the poles
        self.assertAlmostEqual(distance_lat_long(-90, 0, 90, 180), 40030.23060469526)

        # Test case 12: Coordinates at the same longitude but different latitudes
        self.assertAlmostEqual(distance_lat_long(-90, 0, 0, 180), 40030.23060469526)

        # Test case 13: Coordinates at the same latitude but different longitudes
        self.assertAlmostEqual(distance_lat_long(0, -90, 0, 180), 20015.11530234763)

        # Test case 14: Coordinates at the poles
        self.assertAlmostEqual(distance_lat_long(90, 0, -90, 180), 40030.23060469526)

        # Test case 15: Coordinates at the same longitude but different latitudes
        self.assertAlmostEqual(distance_lat_long(90, 0, 0, 180), 40030.23060469526)

        # Test case 16: Coordinates at the same latitude but different longitudes
        self.assert