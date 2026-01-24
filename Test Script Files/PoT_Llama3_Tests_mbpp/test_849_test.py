import unittest
from mbpp_849_code import Sum

class TestSum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(Sum(10), 8)

    def test_edge_case(self):
        self.assertEqual(Sum(1), 0)

    def test_edge_case2(self):
        self.assertEqual(Sum(2), 2)

    def test_edge_case3(self):
        self.assertEqual(Sum(3), 3)

    def test_edge_case4(self):
        self.assertEqual(Sum(4), 3)

    def test_edge_case5(self):
        self.assertEqual(Sum(5), 5)

    def test_edge_case6(self):
        self.assertEqual(Sum(6), 6)

    def test_edge_case7(self):
        self.assertEqual(Sum(7), 7)

    def test_edge_case8(self):
        self.assertEqual(Sum(8), 8)

    def test_edge_case9(self):
        self.assertEqual(Sum(9), 8)

    def test_edge_case10(self):
        self.assertEqual(Sum(10), 8)

    def test_edge_case11(self):
        self.assertEqual(Sum(11), 10)

    def test_edge_case12(self):
        self.assertEqual(Sum(12), 10)

    def test_edge_case13(self):
        self.assertEqual(Sum(13), 12)

    def test_edge_case14(self):
        self.assertEqual(Sum(14), 12)

    def test_edge_case15(self):
        self.assertEqual(Sum(15), 12)

    def test_edge_case16(self):
        self.assertEqual(Sum(16), 14)

    def test_edge_case17(self):
        self.assertEqual(Sum(17), 14)

    def test_edge_case18(self):
        self.assertEqual(Sum(18), 14)

    def test_edge_case19(self):
        self.assertEqual(Sum(19), 16)

    def test_edge_case20(self):
        self.assertEqual(Sum(20), 16)
