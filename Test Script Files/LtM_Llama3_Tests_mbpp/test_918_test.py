import unittest
from mbpp_918_code import coin_change

class TestCoinChange(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(coin_change(2, 3, 4), 1)

    def test_edge_case1(self):
        self.assertEqual(coin_change(0, 3, 4), 0)

    def test_edge_case2(self):
        self.assertEqual(coin_change(4, 3, 4), 1)

    def test_edge_case3(self):
        self.assertEqual(coin_change(5, 3, 4), 0)

    def test_edge_case4(self):
        self.assertEqual(coin_change(1, 3, 4), 1)

    def test_edge_case5(self):
        self.assertEqual(coin_change(3, 3, 4), 1)

    def test_edge_case6(self):
        self.assertEqual(coin_change(4, 3, 3), 0)

    def test_edge_case7(self):
        self.assertEqual(coin_change(5, 3, 3), 0)

    def test_edge_case8(self):
        self.assertEqual(coin_change(6, 3, 3), 0)

    def test_edge_case9(self):
        self.assertEqual(coin_change(7, 3, 3), 0)

    def test_edge_case10(self):
        self.assertEqual(coin_change(8, 3, 3), 0)

    def test_edge_case11(self):
        self.assertEqual(coin_change(9, 3, 3), 0)

    def test_edge_case12(self):
        self.assertEqual(coin_change(10, 3, 3), 0)

    def test_edge_case13(self):
        self.assertEqual(coin_change(11, 3, 3), 0)

    def test_edge_case14(self):
        self.assertEqual(coin_change(12, 3, 3), 0)

    def test_edge_case15(self):
        self.assertEqual(coin_change(13, 3, 3), 0)

    def test_edge_case16(self):
        self.assertEqual(coin_change(14, 3, 3), 0)

    def test_edge_case17(self):
        self.assertEqual(coin_change(15, 3, 3), 0)

    def test_edge_case18(self):
        self.assertEqual(coin_change(16, 3, 3), 0)

    def test_edge_case19(self):
        self.assertEqual(coin_change(17, 3, 3), 0)

    def test_edge_case20(self):
        self.assertEqual(coin_change(18, 3, 3), 0)

    def test_edge_case21(self):
        self.assertEqual(coin_change(19, 3, 3), 0)

    def test_edge_case22(self):
        self.assertEqual(coin_change(20, 3, 3), 0)

    def test_edge_case23(self):
        self.assertEqual(coin_change(21, 3, 3), 0)

    def test_edge_case24(self):
        self.assertEqual(coin_change(22, 3, 3), 0)

    def test_edge_case25(self):
        self.assertEqual(coin_change(23, 3, 3), 0)

    def test_edge_case26(self):
        self.assertEqual(coin_change(24, 3, 3), 0)

    def test_edge_case27(self):
        self.assertEqual(coin_change(25, 3, 3), 0)

    def test_edge_case28(self):
        self.assertEqual(coin_change(26, 3, 3), 0)

    def test_edge_case29(self):
        self.assertEqual(coin_change(27, 3, 3), 0)

    def test_edge_case30(self):
        self.assertEqual(coin_change(28, 3, 3), 0)
