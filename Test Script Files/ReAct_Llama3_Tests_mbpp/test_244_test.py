import unittest
from mbpp_244_code import next_Perfect_Square

class TestNextPerfectSquare(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(next_Perfect_Square(16), 25)

    def test_edge_case(self):
        self.assertEqual(next_Perfect_Square(25), 25)

    def test_edge_case2(self):
        self.assertEqual(next_Perfect_Square(36), 49)

    def test_edge_case3(self):
        self.assertEqual(next_Perfect_Square(100), 100)

    def test_edge_case4(self):
        self.assertEqual(next_Perfect_Square(121), 144)

    def test_edge_case5(self):
        self.assertEqual(next_Perfect_Square(144), 169)

    def test_edge_case6(self):
        self.assertEqual(next_Perfect_Square(169), 196)

    def test_edge_case7(self):
        self.assertEqual(next_Perfect_Square(196), 225)

    def test_edge_case8(self):
        self.assertEqual(next_Perfect_Square(225), 256)

    def test_edge_case9(self):
        self.assertEqual(next_Perfect_Square(256), 289)

    def test_edge_case10(self):
        self.assertEqual(next_Perfect_Square(289), 324)

    def test_edge_case11(self):
        self.assertEqual(next_Perfect_Square(324), 361)

    def test_edge_case12(self):
        self.assertEqual(next_Perfect_Square(361), 400)

    def test_edge_case13(self):
        self.assertEqual(next_Perfect_Square(400), 441)

    def test_edge_case14(self):
        self.assertEqual(next_Perfect_Square(441), 484)

    def test_edge_case15(self):
        self.assertEqual(next_Perfect_Square(484), 529)

    def test_edge_case16(self):
        self.assertEqual(next_Perfect_Square(529), 576)

    def test_edge_case17(self):
        self.assertEqual(next_Perfect_Square(576), 625)

    def test_edge_case18(self):
        self.assertEqual(next_Perfect_Square(625), 676)

    def test_edge_case19(self):
        self.assertEqual(next_Perfect_Square(676), 729)

    def test_edge_case20(self):
        self.assertEqual(next_Perfect_Square(729), 784)

    def test_edge_case21(self):
        self.assertEqual(next_Perfect_Square(784), 841)

    def test_edge_case22(self):
        self.assertEqual(next_Perfect_Square(841), 900)

    def test_edge_case23(self):
        self.assertEqual(next_Perfect_Square(900), 961)

    def test_edge_case24(self):
        self.assertEqual(next_Perfect_Square(961), 1024)

    def test_edge_case25(self):
        self.assertEqual(next_Perfect_Square(1024), 1089)

    def test_edge_case26(self):
        self.assertEqual(next_Perfect_Square(1089), 1156)

    def test_edge_case27(self):
        self.assertEqual(next_Perfect_Square(1156), 1225)

    def test_edge_case28(self):
        self.assertEqual(next_Perfect_Square(1225), 1296)

    def test_edge_case29(self):
        self.assertEqual(next_Perfect_Square(1296), 1369)

    def test_edge_case30(self):
        self.assertEqual(next_Perfect_Square(1369), 1444)

    def test_edge_case31(self):
        self.assertEqual(next_Perfect_Square(1444), 1521)

    def test_edge_case32(self):
        self.assertEqual(next_Perfect_Square(1521), 1600)

    def test_edge_case33(self):
        self.assertEqual(next_Perfect_Square(1600), 1681)

    def test_edge_case34(self):
        self.assertEqual(next_Perfect_Square(1681), 1764)

    def test_edge_case35(self):
        self.assertEqual(next_Perfect_Square(1764), 1849)

    def test_edge_case36(self):
        self.assertEqual(next_Perfect_Square(1849), 1936)

    def test_edge_case37(self):
        self.assertEqual(next_Perfect_Square(1936), 2025)

    def test_edge_case38(self):
        self.assertEqual(next_Perfect_Square(2025), 2124)

    def test_edge_case39(self):
        self.assertEqual(next_Perfect_Square(2124), 2209)

    def test_edge_case40(self):
        self.assertEqual(next_Perfect_Square(2209), 2304)

    def test_edge_case41(self):
        self.assertEqual(next_Perfect_Square(2304), 2401)

    def test_edge_case42(self):
        self.assertEqual(next_Perfect_Square(2401), 2500)

    def test_edge_case43(self):
        self.assertEqual(next_Perfect_Square(250