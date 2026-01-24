import unittest
from mbpp_808_code import check_K

class TestCheckK(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(check_K((1, 2, 3, 4), 3))

    def test_edge_case(self):
        self.assertFalse(check_K((1, 2, 3, 4), 5))

    def test_edge_case2(self):
        self.assertTrue(check_K((1, 2, 3, 4), 1))

    def test_edge_case3(self):
        self.assertFalse(check_K((1, 2, 3, 4), 0))

    def test_edge_case4(self):
        self.assertFalse(check_K((1, 2, 3, 4), 6))

    def test_edge_case5(self):
        self.assertTrue(check_K((1, 2, 3, 4), 4))

    def test_edge_case6(self):
        self.assertFalse(check_K((1, 2, 3, 4), 7))

    def test_edge_case7(self):
        self.assertTrue(check_K((1, 2, 3, 4), 2))

    def test_edge_case8(self):
        self.assertFalse(check_K((1, 2, 3, 4), 8))

    def test_edge_case9(self):
        self.assertFalse(check_K((1, 2, 3, 4), 9))

    def test_edge_case10(self):
        self.assertTrue(check_K((1, 2, 3, 4), 1))

    def test_edge_case11(self):
        self.assertFalse(check_K((1, 2, 3, 4), 10))

    def test_edge_case12(self):
        self.assertFalse(check_K((1, 2, 3, 4), 11))

    def test_edge_case13(self):
        self.assertTrue(check_K((1, 2, 3, 4), 3))

    def test_edge_case14(self):
        self.assertFalse(check_K((1, 2, 3, 4), 12))

    def test_edge_case15(self):
        self.assertFalse(check_K((1, 2, 3, 4), 13))

    def test_edge_case16(self):
        self.assertTrue(check_K((1, 2, 3, 4), 1))

    def test_edge_case17(self):
        self.assertFalse(check_K((1, 2, 3, 4), 14))

    def test_edge_case18(self):
        self.assertFalse(check_K((1, 2, 3, 4), 15))

    def test_edge_case19(self):
        self.assertTrue(check_K((1, 2, 3, 4), 3))

    def test_edge_case20(self):
        self.assertFalse(check_K((1, 2, 3, 4), 16))

    def test_edge_case21(self):
        self.assertFalse(check_K((1, 2, 3, 4), 17))

    def test_edge_case22(self):
        self.assertTrue(check_K((1, 2, 3, 4), 1))

    def test_edge_case23(self):
        self.assertFalse(check_K((1, 2, 3, 4), 18))

    def test_edge_case24(self):
        self.assertFalse(check_K((1, 2, 3, 4), 19))

    def test_edge_case25(self):
        self.assertTrue(check_K((1, 2, 3, 4), 3))

    def test_edge_case26(self):
        self.assertFalse(check_K((1, 2, 3, 4), 20))

    def test_edge_case27(self):
        self.assertFalse(check_K((1, 2, 3, 4), 21))

    def test_edge_case28(self):
        self.assertTrue(check_K((1, 2, 3, 4), 1))

    def test_edge_case29(self):
        self.assertFalse(check_K((1, 2, 3, 4), 22))

    def test_edge_case30(self):
        self.assertFalse(check_K((1, 2, 3, 4), 23))

    def test_edge_case31(self):
        self.assertTrue(check_K((1, 2, 3, 4), 3))

    def test_edge_case32(self):
        self.assertFalse(check_K((1, 2, 3, 4), 24))

    def test_edge_case33(self):
        self.assertFalse(check_K((1, 2, 3, 4), 25))

    def test_edge_case34(self):
        self.assertTrue(check_K((1, 2, 3, 4), 1))

    def test_edge_case35(self):
        self.assertFalse(check_K((1, 2, 3, 4), 26