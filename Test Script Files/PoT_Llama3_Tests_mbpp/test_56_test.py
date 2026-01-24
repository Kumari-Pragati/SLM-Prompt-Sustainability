import unittest
from mbpp_56_code import check

class TestCheckFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check(1))

    def test_edge_case(self):
        self.assertFalse(check(0))

    def test_edge_case2(self):
        self.assertFalse(check(2))

    def test_edge_case3(self):
        self.assertTrue(check(3))

    def test_edge_case4(self):
        self.assertFalse(check(4))

    def test_edge_case5(self):
        self.assertFalse(check(5))

    def test_edge_case6(self):
        self.assertFalse(check(6))

    def test_edge_case7(self):
        self.assertFalse(check(7))

    def test_edge_case8(self):
        self.assertFalse(check(8))

    def test_edge_case9(self):
        self.assertFalse(check(9))

    def test_edge_case10(self):
        self.assertFalse(check(10))

    def test_edge_case11(self):
        self.assertFalse(check(11))

    def test_edge_case12(self):
        self.assertFalse(check(12))

    def test_edge_case13(self):
        self.assertFalse(check(13))

    def test_edge_case14(self):
        self.assertFalse(check(14))

    def test_edge_case15(self):
        self.assertFalse(check(15))

    def test_edge_case16(self):
        self.assertFalse(check(16))

    def test_edge_case17(self):
        self.assertFalse(check(17))

    def test_edge_case18(self):
        self.assertFalse(check(18))

    def test_edge_case19(self):
        self.assertFalse(check(19))

    def test_edge_case20(self):
        self.assertFalse(check(20))

    def test_edge_case21(self):
        self.assertFalse(check(21))

    def test_edge_case22(self):
        self.assertFalse(check(22))

    def test_edge_case23(self):
        self.assertFalse(check(23))

    def test_edge_case24(self):
        self.assertFalse(check(24))

    def test_edge_case25(self):
        self.assertFalse(check(25))

    def test_edge_case26(self):
        self.assertFalse(check(26))

    def test_edge_case27(self):
        self.assertFalse(check(27))

    def test_edge_case28(self):
        self.assertFalse(check(28))

    def test_edge_case29(self):
        self.assertFalse(check(29))

    def test_edge_case30(self):
        self.assertFalse(check(30))
