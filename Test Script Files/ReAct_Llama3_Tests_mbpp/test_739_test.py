import unittest
from mbpp_739_code import find_Index

class TestFindIndex(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Index(1), 10)

    def test_edge_case(self):
        self.assertEqual(find_Index(-1), 10)

    def test_edge_case2(self):
        self.assertEqual(find_Index(0), 1)

    def test_edge_case3(self):
        self.assertEqual(find_Index(2), 10)

    def test_edge_case4(self):
        self.assertEqual(find_Index(3), 31.622776601683793)

    def test_edge_case5(self):
        self.assertEqual(find_Index(4), 100)

    def test_edge_case6(self):
        self.assertEqual(find_Index(5), 316.22776660168394)

    def test_edge_case7(self):
        self.assertEqual(find_Index(6), 1000)

    def test_edge_case8(self):
        self.assertEqual(find_Index(7), 3162.2776601683794)

    def test_edge_case9(self):
        self.assertEqual(find_Index(8), 10000)

    def test_edge_case10(self):
        self.assertEqual(find_Index(9), 31622.776601683794)

    def test_edge_case11(self):
        self.assertEqual(find_Index(10), 100000)

    def test_edge_case12(self):
        self.assertEqual(find_Index(11), 316227.766601683794)

    def test_edge_case13(self):
        self.assertEqual(find_Index(12), 1000000)

    def test_edge_case14(self):
        self.assertEqual(find_Index(13), 31622777660168379)

    def test_edge_case15(self):
        self.assertEqual(find_Index(14), 10000000)

    def test_edge_case16(self):
        self.assertEqual(find_Index(15), 316227766601683794)

    def test_edge_case17(self):
        self.assertEqual(find_Index(16), 100000000)

    def test_edge_case18(self):
        self.assertEqual(find_Index(17), 316227776601683794)

    def test_edge_case19(self):
        self.assertEqual(find_Index(18), 1000000000)

    def test_edge_case20(self):
        self.assertEqual(find_Index(19), 316227766601683794)

    def test_edge_case21(self):
        self.assertEqual(find_Index(20), 10000000000)

    def test_edge_case22(self):
        self.assertEqual(find_Index(21), 316227776601683794)

    def test_edge_case23(self):
        self.assertEqual(find_Index(22), 10000000000)

    def test_edge_case24(self):
        self.assertEqual(find_Index(23), 316227766601683794)

    def test_edge_case25(self):
        self.assertEqual(find_Index(24), 10000000000)

    def test_edge_case26(self):
        self.assertEqual(find_Index(25), 316227776601683794)

    def test_edge_case27(self):
        self.assertEqual(find_Index(26), 10000000000)

    def test_edge_case28(self):
        self.assertEqual(find_Index(27), 316227766601683794)

    def test_edge_case29(self):
        self.assertEqual(find_Index(28), 10000000000)

    def test_edge_case30(self):
        self.assertEqual(find_Index(29), 316227776601683794)

    def test_edge_case31(self):
        self.assertEqual(find_Index(30), 10000000000)

    def test_edge_case32(self):
        self.assertEqual(find_Index(31), 316227766601683794)

    def test_edge_case33(self):
        self.assertEqual(find_Index(32), 10000000000)

    def test_edge_case34(self):
        self.assertEqual(find_Index(33), 316227776601683794)

    def test_edge_case35(self):
        self.assertEqual(find_Index(34), 10000000000)

    def test_edge_case36(self):
        self.assertEqual(find_Index(35), 316227766601683794)

    def test_edge_case37(self):
        self.assertEqual(find_Index(36), 10000000000)

    def test_edge_case38(self):
        self.assertEqual(find_Index(37), 316227776601683794)

    def test_edge_case39(self):
        self.assertEqual(find_Index(38), 10000000000)

    def test_edge_case40(self):
        self.assertEqual(find_Index(39), 316227766601683794)

    def test_edge_case41(self):
        self.assertEqual(find_Index(40), 10000000000)

    def test_edge_case42(self):
        self.assertEqual(find_Index(41), 316227776601683794)

    def test_edge_case43(self):
        self.assertEqual(find_Index(42), 10000000000)

    def test_edge_case44(self):
        self.assertEqual(find_Index(43