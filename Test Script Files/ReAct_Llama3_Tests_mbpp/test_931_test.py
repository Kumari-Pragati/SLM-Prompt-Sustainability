import unittest
from mbpp_931_code import sum_series

class TestSumSeries(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_series(5), 55.0)

    def test_edge_case(self):
        self.assertEqual(sum_series(0), 0.0)

    def test_edge_case2(self):
        self.assertEqual(sum_series(1), 1.0)

    def test_edge_case3(self):
        self.assertEqual(sum_series(-1), 0.0)

    def test_edge_case4(self):
        self.assertEqual(sum_series(-5), 0.0)

    def test_edge_case5(self):
        self.assertEqual(sum_series(10), 385.0)

    def test_edge_case6(self):
        self.assertEqual(sum_series(-10), 0.0)

    def test_edge_case7(self):
        self.assertEqual(sum_series(20), 2100.0)

    def test_edge_case8(self):
        self.assertEqual(sum_series(-20), 0.0)

    def test_edge_case9(self):
        self.assertEqual(sum_series(30), 4650.0)

    def test_edge_case10(self):
        self.assertEqual(sum_series(-30), 0.0)

    def test_edge_case11(self):
        self.assertEqual(sum_series(40), 6800.0)

    def test_edge_case12(self):
        self.assertEqual(sum_series(-40), 0.0)

    def test_edge_case13(self):
        self.assertEqual(sum_series(50), 12750.0)

    def test_edge_case14(self):
        self.assertEqual(sum_series(-50), 0.0)

    def test_edge_case15(self):
        self.assertEqual(sum_series(60), 18660.0)

    def test_edge_case16(self):
        self.assertEqual(sum_series(-60), 0.0)

    def test_edge_case17(self):
        self.assertEqual(sum_series(70), 26460.0)

    def test_edge_case18(self):
        self.assertEqual(sum_series(-70), 0.0)

    def test_edge_case19(self):
        self.assertEqual(sum_series(80), 35680.0)

    def test_edge_case20(self):
        self.assertEqual(sum_series(-80), 0.0)

    def test_edge_case21(self):
        self.assertEqual(sum_series(90), 45590.0)

    def test_edge_case22(self):
        self.assertEqual(sum_series(-90), 0.0)

    def test_edge_case23(self):
        self.assertEqual(sum_series(100), 60500.0)

    def test_edge_case24(self):
        self.assertEqual(sum_series(-100), 0.0)

    def test_edge_case25(self):
        self.assertEqual(sum_series(200), 210200.0)

    def test_edge_case26(self):
        self.assertEqual(sum_series(-200), 0.0)

    def test_edge_case27(self):
        self.assertEqual(sum_series(300), 450300.0)

    def test_edge_case28(self):
        self.assertEqual(sum_series(-300), 0.0)

    def test_edge_case29(self):
        self.assertEqual(sum_series(400), 680400.0)

    def test_edge_case30(self):
        self.assertEqual(sum_series(-400), 0.0)

    def test_edge_case31(self):
        self.assertEqual(sum_series(500), 990500.0)

    def test_edge_case32(self):
        self.assertEqual(sum_series(-500), 0.0)

    def test_edge_case33(self):
        self.assertEqual(sum_series(600), 1276500.0)

    def test_edge_case34(self):
        self.assertEqual(sum_series(-600), 0.0)

    def test_edge_case35(self):
        self.assertEqual(sum_series(700), 2647000.0)

    def test_edge_case36(self):
        self.assertEqual(sum_series(-700), 0.0)

    def test_edge_case37(self):
        self.assertEqual(sum_series(800), 3568000.0)

    def test_edge_case38(self):
        self.assertEqual(sum_series(-800), 0.0)

    def test_edge_case39(self):
        self.assertEqual(sum_series(900), 4559000.0)

    def test_edge_case40(self):
        self.assertEqual(sum_series(-900), 0.0)

    def test_edge_case41(self):
        self.assertEqual(sum_series(1000), 6050000.0)

    def test_edge_case42(self):
        self.assertEqual(sum_series(-1000), 0.0)

    def test_edge_case43(self):
        self.assertEqual(sum_series(2000), 21020000.0)

    def test_edge_case44(self):
        self.assertEqual(sum_series(-2000), 0.0)

    def test_edge_case45(self):
        self.assertEqual(sum_series(3000), 45030000.0)

    def test_edge_case46(self