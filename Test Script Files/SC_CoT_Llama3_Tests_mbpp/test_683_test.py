import unittest
from mbpp_683_code import sum_Square

class TestSumSquare(unittest.TestCase):
    def test_true(self):
        self.assertTrue(sum_Square(5))

    def test_false(self):
        self.assertFalse(sum_Square(10))

    def test_edge_case(self):
        self.assertTrue(sum_Square(4))

    def test_edge_case2(self):
        self.assertFalse(sum_Square(15))

    def test_edge_case3(self):
        self.assertTrue(sum_Square(9))

    def test_edge_case4(self):
        self.assertFalse(sum_Square(20))

    def test_edge_case5(self):
        self.assertTrue(sum_Square(8))

    def test_edge_case6(self):
        self.assertFalse(sum_Square(25))

    def test_edge_case7(self):
        self.assertTrue(sum_Square(7))

    def test_edge_case8(self):
        self.assertFalse(sum_Square(30))

    def test_edge_case9(self):
        self.assertTrue(sum_Square(1))

    def test_edge_case10(self):
        self.assertFalse(sum_Square(36))

    def test_edge_case11(self):
        self.assertTrue(sum_Square(0))

    def test_edge_case12(self):
        self.assertFalse(sum_Square(40))

    def test_edge_case13(self):
        self.assertTrue(sum_Square(4))

    def test_edge_case14(self):
        self.assertFalse(sum_Square(50))

    def test_edge_case15(self):
        self.assertTrue(sum_Square(9))

    def test_edge_case16(self):
        self.assertFalse(sum_Square(60))

    def test_edge_case17(self):
        self.assertTrue(sum_Square(16))

    def test_edge_case18(self):
        self.assertFalse(sum_Square(70))

    def test_edge_case19(self):
        self.assertTrue(sum_Square(25))

    def test_edge_case20(self):
        self.assertFalse(sum_Square(80))

    def test_edge_case21(self):
        self.assertTrue(sum_Square(36))

    def test_edge_case22(self):
        self.assertFalse(sum_Square(90))

    def test_edge_case23(self):
        self.assertTrue(sum_Square(49))

    def test_edge_case24(self):
        self.assertFalse(sum_Square(100))
