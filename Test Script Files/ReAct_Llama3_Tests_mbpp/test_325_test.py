import unittest
from mbpp_325_code import get_Min_Squares

class TestGetMinSquares(unittest.TestCase):
    def test_get_Min_Squares_typical(self):
        self.assertEqual(get_Min_Squares(12), 3)

    def test_get_Min_Squares_edge_case1(self):
        self.assertEqual(get_Min_Squares(3), 3)

    def test_get_Min_Squares_edge_case2(self):
        self.assertEqual(get_Min_Squares(4), 1)

    def test_get_Min_Squares_edge_case3(self):
        self.assertEqual(get_Min_Squares(9), 2)

    def test_get_Min_Squares_edge_case4(self):
        self.assertEqual(get_Min_Squares(10), 2)

    def test_get_Min_Squares_edge_case5(self):
        self.assertEqual(get_Min_Squares(15), 3)

    def test_get_Min_Squares_edge_case6(self):
        self.assertEqual(get_Min_Squares(16), 4)

    def test_get_Min_Squares_edge_case7(self):
        self.assertEqual(get_Min_Squares(20), 4)

    def test_get_Min_Squares_edge_case8(self):
        self.assertEqual(get_Min_Squares(25), 5)

    def test_get_Min_Squares_edge_case9(self):
        self.assertEqual(get_Min_Squares(30), 5)

    def test_get_Min_Squares_edge_case10(self):
        self.assertEqual(get_Min_Squares(36), 6)

    def test_get_Min_Squares_edge_case11(self):
        self.assertEqual(get_Min_Squares(40), 6)

    def test_get_Min_Squares_edge_case12(self):
        self.assertEqual(get_Min_Squares(45), 6)

    def test_get_Min_Squares_edge_case13(self):
        self.assertEqual(get_Min_Squares(50), 7)

    def test_get_Min_Squares_edge_case14(self):
        self.assertEqual(get_Min_Squares(60), 7)

    def test_get_Min_Squares_edge_case15(self):
        self.assertEqual(get_Min_Squares(64), 8)

    def test_get_Min_Squares_edge_case16(self):
        self.assertEqual(get_Min_Squares(81), 9)

    def test_get_Min_Squares_edge_case17(self):
        self.assertEqual(get_Min_Squares(100), 10)

    def test_get_Min_Squares_edge_case18(self):
        self.assertEqual(get_Min_Squares(121), 11)

    def test_get_Min_Squares_edge_case19(self):
        self.assertEqual(get_Min_Squares(144), 12)

    def test_get_Min_Squares_edge_case20(self):
        self.assertEqual(get_Min_Squares(169), 13)

    def test_get_Min_Squares_edge_case21(self):
        self.assertEqual(get_Min_Squares(196), 14)

    def test_get_Min_Squares_edge_case22(self):
        self.assertEqual(get_Min_Squares(225), 15)

    def test_get_Min_Squares_edge_case23(self):
        self.assertEqual(get_Min_Squares(256), 16)

    def test_get_Min_Squares_edge_case24(self):
        self.assertEqual(get_Min_Squares(289), 17)

    def test_get_Min_Squares_edge_case25(self):
        self.assertEqual(get_Min_Squares(324), 18)

    def test_get_Min_Squares_edge_case26(self):
        self.assertEqual(get_Min_Squares(361), 19)

    def test_get_Min_Squares_edge_case27(self):
        self.assertEqual(get_Min_Squares(400), 20)

    def test_get_Min_Squares_edge_case28(self):
        self.assertEqual(get_Min_Squares(441), 21)

    def test_get_Min_Squares_edge_case29(self):
        self.assertEqual(get_Min_Squares(484), 22)

    def test_get_Min_Squares_edge_case30(self):
        self.assertEqual(get_Min_Squares(529), 23)

    def test_get_Min_Squares_edge_case31(self):
        self.assertEqual(get_Min_Squares(576), 24)

    def test_get_Min_Squares_edge_case32(self):
        self.assertEqual(get_Min_Squares(625), 25)

    def test_get_Min_Squares_edge_case33(self):
        self.assertEqual(get_Min_Squares(676), 26)

    def test_get_Min_Squares_edge_case34(self):
        self.assertEqual(get_Min_Squares(729), 27)

    def test_get_Min_Squares_edge_case35(self):
        self.assertEqual(get_Min_Squares(784), 28)

    def test_get_Min_Squares_edge_case36(self):
        self.assertEqual(get_Min_Squares(841), 29)

    def test_get_Min_Squares_edge_case37(self):
        self.assertEqual(get_Min_Squares(900), 30)

    def test_get_Min_Squares_edge_case38(self):
        self.assertEqual(get_Min_Squares(961), 31)

    def test_get_Min_Squares_edge_case39(self):
        self.assertEqual(get_Min_Squares(1024), 32)