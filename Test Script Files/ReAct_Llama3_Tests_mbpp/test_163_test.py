import unittest
from mbpp_163_code import area_polygon

class TestAreaPolygon(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(area_polygon(4, 5), 10.0)

    def test_edge_case(self):
        self.assertAlmostEqual(area_polygon(1, 1), 0.0)

    def test_edge_case2(self):
        self.assertAlmostEqual(area_polygon(2, 2), 2.0)

    def test_edge_case3(self):
        self.assertAlmostEqual(area_polygon(3, 3), 6.0)

    def test_edge_case4(self):
        self.assertAlmostEqual(area_polygon(4, 4), 8.0)

    def test_edge_case5(self):
        self.assertAlmostEqual(area_polygon(5, 5), 10.0)

    def test_edge_case6(self):
        self.assertAlmostEqual(area_polygon(6, 6), 12.0)

    def test_edge_case7(self):
        self.assertAlmostEqual(area_polygon(7, 7), 14.0)

    def test_edge_case8(self):
        self.assertAlmostEqual(area_polygon(8, 8), 16.0)

    def test_edge_case9(self):
        self.assertAlmostEqual(area_polygon(9, 9), 18.0)

    def test_edge_case10(self):
        self.assertAlmostEqual(area_polygon(10, 10), 20.0)

    def test_edge_case11(self):
        self.assertAlmostEqual(area_polygon(11, 11), 22.0)

    def test_edge_case12(self):
        self.assertAlmostEqual(area_polygon(12, 12), 24.0)

    def test_edge_case13(self):
        self.assertAlmostEqual(area_polygon(13, 13), 26.0)

    def test_edge_case14(self):
        self.assertAlmostEqual(area_polygon(14, 14), 28.0)

    def test_edge_case15(self):
        self.assertAlmostEqual(area_polygon(15, 15), 30.0)

    def test_edge_case16(self):
        self.assertAlmostEqual(area_polygon(16, 16), 32.0)

    def test_edge_case17(self):
        self.assertAlmostEqual(area_polygon(17, 17), 34.0)

    def test_edge_case18(self):
        self.assertAlmostEqual(area_polygon(18, 18), 36.0)

    def test_edge_case19(self):
        self.assertAlmostEqual(area_polygon(19, 19), 38.0)

    def test_edge_case20(self):
        self.assertAlmostEqual(area_polygon(20, 20), 40.0)

    def test_edge_case21(self):
        self.assertAlmostEqual(area_polygon(21, 21), 42.0)

    def test_edge_case22(self):
        self.assertAlmostEqual(area_polygon(22, 22), 44.0)

    def test_edge_case23(self):
        self.assertAlmostEqual(area_polygon(23, 23), 46.0)

    def test_edge_case24(self):
        self.assertAlmostEqual(area_polygon(24, 24), 48.0)

    def test_edge_case25(self):
        self.assertAlmostEqual(area_polygon(25, 25), 50.0)

    def test_edge_case26(self):
        self.assertAlmostEqual(area_polygon(26, 26), 52.0)

    def test_edge_case27(self):
        self.assertAlmostEqual(area_polygon(27, 27), 54.0)

    def test_edge_case28(self):
        self.assertAlmostEqual(area_polygon(28, 28), 56.0)

    def test_edge_case29(self):
        self.assertAlmostEqual(area_polygon(29, 29), 58.0)

    def test_edge_case30(self):
        self.assertAlmostEqual(area_polygon(30, 30), 60.0)

    def test_edge_case31(self):
        self.assertAlmostEqual(area_polygon(31, 31), 62.0)

    def test_edge_case32(self):
        self.assertAlmostEqual(area_polygon(32, 32), 64.0)

    def test_edge_case33(self):
        self.assertAlmostEqual(area_polygon(33, 33), 66.0)

    def test_edge_case34(self):
        self.assertAlmostEqual(area_polygon(34, 34), 68.0)

    def test_edge_case35(self):
        self.assertAlmostEqual(area_polygon(35, 35), 70.0)

    def test_edge_case36(self):
        self.assertAlmostEqual(area_polygon(36, 36), 72.0)

    def test_edge_case37(self):
        self.assertAlmostEqual(area_polygon(37, 37), 74.0)

    def test_edge_case38(self):
        self.assertAlmostEqual(area_polygon(38, 38), 76.0)

    def test_edge_case39(self):
        self.assertAlmostEqual(area_polygon(39, 39), 78.0)

    def test_edge_case40(self):
        self.assertAlmostEqual(area_polygon(40, 40), 80.0)

    def test_edge_case41(self):
        self.assertAlmostEqual(area_polygon(41, 41), 82