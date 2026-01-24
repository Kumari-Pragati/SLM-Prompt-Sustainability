import unittest
from mbpp_295_code import sum_div

class TestSumDiv(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_div(10), 18)

    def test_edge_case(self):
        self.assertEqual(sum_div(1), 1)

    def test_edge_case2(self):
        self.assertEqual(sum_div(2), 3)

    def test_edge_case3(self):
        self.assertEqual(sum_div(3), 4)

    def test_edge_case4(self):
        self.assertEqual(sum_div(4), 7)

    def test_edge_case5(self):
        self.assertEqual(sum_div(5), 6)

    def test_edge_case6(self):
        self.assertEqual(sum_div(6), 12)

    def test_edge_case7(self):
        self.assertEqual(sum_div(7), 12)

    def test_edge_case8(self):
        self.assertEqual(sum_div(8), 15)

    def test_edge_case9(self):
        self.assertEqual(sum_div(9), 13)

    def test_edge_case10(self):
        self.assertEqual(sum_div(10), 18)

    def test_edge_case11(self):
        self.assertEqual(sum_div(11), 12)

    def test_edge_case12(self):
        self.assertEqual(sum_div(12), 18)

    def test_edge_case13(self):
        self.assertEqual(sum_div(13), 24)

    def test_edge_case14(self):
        self.assertEqual(sum_div(14), 24)

    def test_edge_case15(self):
        self.assertEqual(sum_div(15), 24)

    def test_edge_case16(self):
        self.assertEqual(sum_div(16), 33)

    def test_edge_case17(self):
        self.assertEqual(sum_div(17), 24)

    def test_edge_case18(self):
        self.assertEqual(sum_div(18), 39)

    def test_edge_case19(self):
        self.assertEqual(sum_div(19), 39)

    def test_edge_case20(self):
        self.assertEqual(sum_div(20), 42)

    def test_edge_case21(self):
        self.assertEqual(sum_div(21), 42)

    def test_edge_case22(self):
        self.assertEqual(sum_div(22), 45)

    def test_edge_case23(self):
        self.assertEqual(sum_div(23), 45)

    def test_edge_case24(self):
        self.assertEqual(sum_div(24), 60)

    def test_edge_case25(self):
        self.assertEqual(sum_div(25), 60)
