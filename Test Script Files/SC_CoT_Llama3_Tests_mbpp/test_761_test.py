import unittest
from mbpp_761_code import arc_length

class TestArcLength(unittest.TestCase):

    def test_typical_input(self):
        self.assertAlmostEqual(arc_length(10, 30), 3.142857142857143)

    def test_edge_case(self):
        self.assertIsNone(arc_length(10, 360))

    def test_edge_case_2(self):
        self.assertAlmostEqual(arc_length(10, 0), 0)

    def test_edge_case_3(self):
        self.assertAlmostEqual(arc_length(10, 360), 0)

    def test_edge_case_4(self):
        self.assertIsNone(arc_length(10, 720))

    def test_edge_case_5(self):
        self.assertAlmostEqual(arc_length(10, 90), 3.142857142857143)

    def test_edge_case_6(self):
        self.assertIsNone(arc_length(10, 900))

    def test_edge_case_7(self):
        self.assertAlmostEqual(arc_length(10, 180), 6.285714285714286)

    def test_edge_case_8(self):
        self.assertIsNone(arc_length(10, 1080))

    def test_edge_case_9(self):
        self.assertAlmostEqual(arc_length(10, 270), 9.428571428571429)

    def test_edge_case_10(self):
        self.assertIsNone(arc_length(10, 1620))

    def test_edge_case_11(self):
        self.assertAlmostEqual(arc_length(10, 360), 0)

    def test_edge_case_12(self):
        self.assertIsNone(arc_length(10, 2160))

    def test_edge_case_13(self):
        self.assertAlmostEqual(arc_length(10, 540), 17.142857142857143)

    def test_edge_case_14(self):
        self.assertIsNone(arc_length(10, 2520))

    def test_edge_case_15(self):
        self.assertAlmostEqual(arc_length(10, 720), 0)

    def test_edge_case_16(self):
        self.assertIsNone(arc_length(10, 2880))

    def test_edge_case_17(self):
        self.assertAlmostEqual(arc_length(10, 1080), 0)

    def test_edge_case_18(self):
        self.assertIsNone(arc_length(10, 3240))

    def test_edge_case_19(self):
        self.assertAlmostEqual(arc_length(10, 1620), 0)

    def test_edge_case_20(self):
        self.assertIsNone(arc_length(10, 3600))
