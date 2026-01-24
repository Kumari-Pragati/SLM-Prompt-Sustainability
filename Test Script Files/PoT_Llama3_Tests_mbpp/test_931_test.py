import unittest
from mbpp_931_code import sum_series

class TestSumSeries(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sum_series(5), 25.0)

    def test_edge_case(self):
        self.assertEqual(sum_series(0), 0.0)

    def test_edge_case2(self):
        self.assertEqual(sum_series(1), 1.0)

    def test_edge_case3(self):
        self.assertEqual(sum_series(-1), 0.0)

    def test_edge_case4(self):
        self.assertEqual(sum_series(-5), 25.0)

    def test_edge_case5(self):
        self.assertEqual(sum_series(10), 100.0)

    def test_edge_case6(self):
        self.assertEqual(sum_series(-10), 100.0)

    def test_edge_case7(self):
        self.assertEqual(sum_series(20), 210.0)

    def test_edge_case8(self):
        self.assertEqual(sum_series(-20), 210.0)

    def test_edge_case9(self):
        self.assertEqual(sum_series(50), 1275.0)

    def test_edge_case10(self):
        self.assertEqual(sum_series(-50), 1275.0)

    def test_edge_case11(self):
        self.assertEqual(sum_series(100), 5050.0)

    def test_edge_case12(self):
        self.assertEqual(sum_series(-100), 5050.0)

    def test_edge_case13(self):
        self.assertEqual(sum_series(200), 21020.0)

    def test_edge_case14(self):
        self.assertEqual(sum_series(-200), 21020.0)

    def test_edge_case15(self):
        self.assertEqual(sum_series(500), 125750.0)

    def test_edge_case16(self):
        self.assertEqual(sum_series(-500), 125750.0)

    def test_edge_case17(self):
        self.assertEqual(sum_series(1000), 250250.0)

    def test_edge_case18(self):
        self.assertEqual(sum_series(-1000), 250250.0)

    def test_edge_case19(self):
        self.assertEqual(sum_series(2000), 210210.0)

    def test_edge_case20(self):
        self.assertEqual(sum_series(-2000), 210210.0)
