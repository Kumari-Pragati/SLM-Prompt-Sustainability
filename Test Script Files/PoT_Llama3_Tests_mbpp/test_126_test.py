import unittest
from mbpp_126_code import sum

class TestSum(unittest.TestCase):

    def test_typical(self):
        self.assertEqual(sum(12, 15), 3)

    def test_edge1(self):
        self.assertEqual(sum(12, 12), 3)

    def test_edge2(self):
        self.assertEqual(sum(1, 1), 0)

    def test_edge3(self):
        self.assertEqual(sum(1, 2), 1)

    def test_edge4(self):
        self.assertEqual(sum(2, 1), 1)

    def test_edge5(self):
        self.assertEqual(sum(4, 4), 2)

    def test_edge6(self):
        self.assertEqual(sum(6, 6), 3)

    def test_edge7(self):
        self.assertEqual(sum(8, 8), 4)

    def test_edge8(self):
        self.assertEqual(sum(10, 10), 5)

    def test_edge9(self):
        self.assertEqual(sum(12, 12), 3)

    def test_edge10(self):
        self.assertEqual(sum(14, 14), 7)

    def test_edge11(self):
        self.assertEqual(sum(16, 16), 8)

    def test_edge12(self):
        self.assertEqual(sum(18, 18), 9)

    def test_edge13(self):
        self.assertEqual(sum(20, 20), 10)

    def test_edge14(self):
        self.assertEqual(sum(22, 22), 11)

    def test_edge15(self):
        self.assertEqual(sum(24, 24), 12)

    def test_edge16(self):
        self.assertEqual(sum(26, 26), 13)

    def test_edge17(self):
        self.assertEqual(sum(28, 28), 14)

    def test_edge18(self):
        self.assertEqual(sum(30, 30), 15)

    def test_edge19(self):
        self.assertEqual(sum(32, 32), 16)

    def test_edge20(self):
        self.assertEqual(sum(34, 34), 17)

    def test_edge21(self):
        self.assertEqual(sum(36, 36), 18)

    def test_edge22(self):
        self.assertEqual(sum(38, 38), 19)

    def test_edge23(self):
        self.assertEqual(sum(40, 40), 20)

    def test_edge24(self):
        self.assertEqual(sum(42, 42), 21)

    def test_edge25(self):
        self.assertEqual(sum(44, 44), 22)

    def test_edge26(self):
        self.assertEqual(sum(46, 46), 23)

    def test_edge27(self):
        self.assertEqual(sum(48, 48), 24)

    def test_edge28(self):
        self.assertEqual(sum(50, 50), 25)

    def test_edge29(self):
        self.assertEqual(sum(52, 52), 26)

    def test_edge30(self):
        self.assertEqual(sum(54, 54), 27)

    def test_edge31(self):
        self.assertEqual(sum(56, 56), 28)

    def test_edge32(self):
        self.assertEqual(sum(58, 58), 29)

    def test_edge33(self):
        self.assertEqual(sum(60, 60), 30)

    def test_edge34(self):
        self.assertEqual(sum(62, 62), 31)

    def test_edge35(self):
        self.assertEqual(sum(64, 64), 32)

    def test_edge36(self):
        self.assertEqual(sum(66, 66), 33)

    def test_edge37(self):
        self.assertEqual(sum(68, 68), 34)

    def test_edge38(self):
        self.assertEqual(sum(70, 70), 35)

    def test_edge39(self):
        self.assertEqual(sum(72, 72), 36)

    def test_edge40(self):
        self.assertEqual(sum(74, 74), 37)

    def test_edge41(self):
        self.assertEqual(sum(76, 76), 38)

    def test_edge42(self):
        self.assertEqual(sum(78, 78), 39)

    def test_edge43(self):
        self.assertEqual(sum(80, 80), 40)

    def test_edge44(self):
        self.assertEqual(sum(82, 82), 41)

    def test_edge45(self):
        self.assertEqual(sum(84, 84), 42)

    def test_edge46(self):
        self.assertEqual(sum(86, 86), 43)

    def test_edge47(self):
        self.assertEqual(sum(88, 88), 44)

    def test_edge48(self):
        self.assertEqual(sum(90, 90), 45)

    def test_edge49(self):
        self.assertEqual(sum(92, 92), 46)

    def test_edge50(self):