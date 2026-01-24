import unittest
from mbpp_180_code import distance_lat_long

class TestDistanceLatLong(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, 0), 0, places=5)

    def test_edge_case(self):
        self.assertAlmostEqual(distance_lat_long(0, 0, 90, 0), 3.14159265359, places=5)

    def test_edge_case2(self):
        self.assertAlmostEqual(distance_lat_long(0, 0, -90, 0), 3.14159265359, places=5)

    def test_edge_case3(self):
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, 180), 6.28318530718, places=5)

    def test_edge_case4(self):
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, 360), 6.28318530718, places=5)

    def test_edge_case5(self):
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, 90), 3.14159265359, places=5)

    def test_edge_case6(self):
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, -90), 3.14159265359, places=5)

    def test_edge_case7(self):
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, 0), 0, places=5)

    def test_edge_case8(self):
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, 180), 6.28318530718, places=5)

    def test_edge_case9(self):
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, 360), 6.28318530718, places=5)

    def test_edge_case10(self):
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, 90), 3.14159265359, places=5)

    def test_edge_case11(self):
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, -90), 3.14159265359, places=5)

    def test_edge_case12(self):
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, 0), 0, places=5)

    def test_edge_case13(self):
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, 180), 6.28318530718, places=5)

    def test_edge_case14(self):
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, 360), 6.28318530718, places=5)

    def test_edge_case15(self):
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, 90), 3.14159265359, places=5)

    def test_edge_case16(self):
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, -90), 3.14159265359, places=5)

    def test_edge_case17(self):
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, 0), 0, places=5)

    def test_edge_case18(self):
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, 180), 6.28318530718, places=5)

    def test_edge_case19(self):
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, 360), 6.28318530718, places=5)

    def test_edge_case20(self):
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, 90), 3.14159265359, places=5)

    def test_edge_case21(self):
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, -90), 3.14159265359, places=5)

    def test_edge_case22(self):
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, 0), 0, places=5)

    def test_edge_case23(self):
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, 180), 6.28318530718, places=5)

    def test_edge_case24(self):
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, 360), 6.28318530718, places=5)

    def test_edge_case25(self):
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, 90), 3.14159265359, places=5)

    def test_edge_case26(self):
        self.assertAlmostEqual(distance_lat_long(0, 0, 0, -90), 3.14159265359, places=5)

    def test_edge