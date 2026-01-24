import unittest
from mbpp_327_code import check_isosceles

class TestCheckIsosceles(unittest.TestCase):
    def test_simple_true(self):
        self.assertTrue(check_isosceles(3, 3, 3))

    def test_simple_false(self):
        self.assertFalse(check_isosceles(1, 2, 3))

    def test_edge_equal(self):
        self.assertTrue(check_isosceles(2, 2, 2))

    def test_edge_nearest(self):
        self.assertTrue(check_isosceles(2, 3, 3))

    def test_edge_farthest(self):
        self.assertTrue(check_isosceles(1, 3, 3))

    def test_edge_reverse(self):
        self.assertTrue(check_isosceles(3, 2, 2))

    def test_edge_reverse2(self):
        self.assertTrue(check_isosceles(3, 3, 2))

    def test_edge_reverse3(self):
        self.assertTrue(check_isosceles(2, 3, 1))

    def test_edge_reverse4(self):
        self.assertTrue(check_isosceles(2, 2, 1))

    def test_edge_reverse5(self):
        self.assertTrue(check_isosceles(1, 2, 3))

    def test_edge_reverse6(self):
        self.assertTrue(check_isosceles(1, 3, 2))

    def test_edge_reverse7(self):
        self.assertTrue(check_isosceles(1, 2, 1))

    def test_edge_reverse8(self):
        self.assertTrue(check_isosceles(1, 1, 2))

    def test_edge_reverse9(self):
        self.assertTrue(check_isosceles(1, 1, 1))

    def test_edge_reverse10(self):
        self.assertTrue(check_isosceles(2, 2, 2))

    def test_edge_reverse11(self):
        self.assertTrue(check_isosceles(3, 3, 3))

    def test_edge_reverse12(self):
        self.assertTrue(check_isosceles(2, 3, 3))

    def test_edge_reverse13(self):
        self.assertTrue(check_isosceles(3, 2, 3))

    def test_edge_reverse14(self):
        self.assertTrue(check_isosceles(3, 3, 2))

    def test_edge_reverse15(self):
        self.assertTrue(check_isosceles(2, 2, 3))

    def test_edge_reverse16(self):
        self.assertTrue(check_isosceles(1, 2, 2))

    def test_edge_reverse17(self):
        self.assertTrue(check_isosceles(2, 1, 2))

    def test_edge_reverse18(self):
        self.assertTrue(check_isosceles(2, 2, 1))

    def test_edge_reverse19(self):
        self.assertTrue(check_isosceles(1, 1, 3))

    def test_edge_reverse20(self):
        self.assertTrue(check_isosceles(1, 3, 1))

    def test_edge_reverse21(self):
        self.assertTrue(check_isosceles(1, 2, 2))

    def test_edge_reverse22(self):
        self.assertTrue(check_isosceles(2, 2, 2))

    def test_edge_reverse23(self):
        self.assertTrue(check_isosceles(3, 3, 3))

    def test_edge_reverse24(self):
        self.assertTrue(check_isosceles(2, 3, 3))

    def test_edge_reverse25(self):
        self.assertTrue(check_isosceles(3, 2, 3))

    def test_edge_reverse26(self):
        self.assertTrue(check_isosceles(3, 3, 2))

    def test_edge_reverse27(self):
        self.assertTrue(check_isosceles(2, 2, 3))

    def test_edge_reverse28(self):
        self.assertTrue(check_isosceles(1, 2, 2))

    def test_edge_reverse29(self):
        self.assertTrue(check_isosceles(2, 1, 2))

    def test_edge_reverse30(self):
        self.assertTrue(check_isosceles(2, 2, 1))

    def test_edge_reverse31(self):
        self.assertTrue(check_isosceles(1, 1, 3))

    def test_edge_reverse32(self):
        self.assertTrue(check_isosceles(1, 3, 1))

    def test_edge_reverse33(self):
        self.assertTrue(check_isosceles(1, 2, 2))

    def test_edge_reverse34(self):
        self.assertTrue(check_isosceles(2, 2, 2))

    def test_edge_reverse35(self):
        self.assertTrue(check_isosceles(3, 3, 3))

    def test