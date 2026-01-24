import unittest
from mbpp_853_code import sum_of_odd_Factors

class TestSumOfOddFactors(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sum_of_odd_Factors(10), 10)

    def test_edge_case(self):
        self.assertEqual(sum_of_odd_Factors(1), 1)

    def test_edge_case2(self):
        self.assertEqual(sum_of_odd_Factors(2), 3)

    def test_edge_case3(self):
        self.assertEqual(sum_of_odd_Factors(4), 5)

    def test_edge_case4(self):
        self.assertEqual(sum_of_odd_Factors(9), 13)

    def test_edge_case5(self):
        self.assertEqual(sum_of_odd_Factors(16), 21)

    def test_edge_case6(self):
        self.assertEqual(sum_of_odd_Factors(25), 31)

    def test_edge_case7(self):
        self.assertEqual(sum_of_odd_Factors(36), 43)

    def test_edge_case8(self):
        self.assertEqual(sum_of_odd_Factors(49), 55)

    def test_edge_case9(self):
        self.assertEqual(sum_of_odd_Factors(64), 71)

    def test_edge_case10(self):
        self.assertEqual(sum_of_odd_Factors(81), 89)

    def test_edge_case11(self):
        self.assertEqual(sum_of_odd_Factors(100), 105)

    def test_edge_case12(self):
        self.assertEqual(sum_of_odd_Factors(121), 123)

    def test_edge_case13(self):
        self.assertEqual(sum_of_odd_Factors(144), 147)

    def test_edge_case14(self):
        self.assertEqual(sum_of_odd_Factors(169), 173)

    def test_edge_case15(self):
        self.assertEqual(sum_of_odd_Factors(196), 201)

    def test_edge_case16(self):
        self.assertEqual(sum_of_odd_Factors(225), 231)

    def test_edge_case17(self):
        self.assertEqual(sum_of_odd_Factors(256), 257)

    def test_edge_case18(self):
        self.assertEqual(sum_of_odd_Factors(289), 293)

    def test_edge_case19(self):
        self.assertEqual(sum_of_odd_Factors(324), 327)

    def test_edge_case20(self):
        self.assertEqual(sum_of_odd_Factors(361), 365)

    def test_edge_case21(self):
        self.assertEqual(sum_of_odd_Factors(400), 405)

    def test_edge_case22(self):
        self.assertEqual(sum_of_odd_Factors(441), 447)

    def test_edge_case23(self):
        self.assertEqual(sum_of_odd_Factors(484), 489)

    def test_edge_case24(self):
        self.assertEqual(sum_of_odd_Factors(529), 537)

    def test_edge_case25(self):
        self.assertEqual(sum_of_odd_Factors(576), 585)

    def test_edge_case26(self):
        self.assertEqual(sum_of_odd_Factors(625), 633)

    def test_edge_case27(self):
        self.assertEqual(sum_of_odd_Factors(676), 687)

    def test_edge_case28(self):
        self.assertEqual(sum_of_odd_Factors(729), 741)

    def test_edge_case29(self):
        self.assertEqual(sum_of_odd_Factors(784), 801)

    def test_edge_case30(self):
        self.assertEqual(sum_of_odd_Factors(841), 857)

    def test_edge_case31(self):
        self.assertEqual(sum_of_odd_Factors(900), 913)

    def test_edge_case32(self):
        self.assertEqual(sum_of_odd_Factors(961), 977)

    def test_edge_case33(self):
        self.assertEqual(sum_of_odd_Factors(1024), 1045)

    def test_edge_case34(self):
        self.assertEqual(sum_of_odd_Factors(1089), 1121)

    def test_edge_case35(self):
        self.assertEqual(sum_of_odd_Factors(1225), 1243)

    def test_edge_case36(self):
        self.assertEqual(sum_of_odd_Factors(1331), 1365)

    def test_edge_case37(self):
        self.assertEqual(sum_of_odd_Factors(1444), 1473)

    def test_edge_case38(self):
        self.assertEqual(sum_of_odd_Factors(1555), 1593)

    def test_edge_case39(self):
        self.assertEqual(sum_of_odd_Factors(1666), 1713)

    def test_edge_case40(self):
        self.assertEqual(sum_of_odd_Factors(1777), 1833)

    def test_edge_case41(self):
        self.assertEqual(sum_of_odd_Factors(2000), 2045)

    def test_edge_case42(self):
        self.assertEqual(sum_of_odd_Factors(2209), 2265)

    def test_edge_case43(self):
        self.assertEqual(sum_of_odd_Factors(2425), 2473)

    def test_edge_case44(self):
        self.assertEqual(sum