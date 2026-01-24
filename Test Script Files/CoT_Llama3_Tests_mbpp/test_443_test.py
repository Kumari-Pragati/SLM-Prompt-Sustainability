import unittest
from mbpp_443_code import largest_neg

class TestLargestNeg(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(largest_neg([-10, -5, 0, 5, 10]), -10)

    def test_edge_case(self):
        self.assertEqual(largest_neg([-10, -5, 0]), -10)

    def test_edge_case2(self):
        self.assertEqual(largest_neg([-10, -5, 0, 5]), -10)

    def test_edge_case3(self):
        self.assertEqual(largest_neg([-10, 0, 5, 10]), 0)

    def test_edge_case4(self):
        self.assertEqual(largest_neg([0, 5, 10]), 0)

    def test_edge_case5(self):
        self.assertEqual(largest_neg([10, 20, 30]), 10)

    def test_edge_case6(self):
        self.assertEqual(largest_neg([-10, -5, -3, -1]), -10)

    def test_edge_case7(self):
        self.assertEqual(largest_neg([-10, -5, -3, 0]), -10)

    def test_edge_case8(self):
        self.assertEqual(largest_neg([-10, -5, 0, 5, 10, 15]), -10)

    def test_edge_case9(self):
        self.assertEqual(largest_neg([-10, -5, 0, 5, 10, 15, 20]), -10)

    def test_edge_case10(self):
        self.assertEqual(largest_neg([-10, -5, 0, 5, 10, 15, 20, 25]), -10)

    def test_edge_case11(self):
        self.assertEqual(largest_neg([-10, -5, 0, 5, 10, 15, 20, 25, 30]), -10)

    def test_edge_case12(self):
        self.assertEqual(largest_neg([-10, -5, 0, 5, 10, 15, 20, 25, 30, 35]), -10)

    def test_edge_case13(self):
        self.assertEqual(largest_neg([-10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40]), -10)

    def test_edge_case14(self):
        self.assertEqual(largest_neg([-10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45]), -10)

    def test_edge_case15(self):
        self.assertEqual(largest_neg([-10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]), -10)

    def test_edge_case16(self):
        self.assertEqual(largest_neg([-10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55]), -10)

    def test_edge_case17(self):
        self.assertEqual(largest_neg([-10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]), -10)

    def test_edge_case18(self):
        self.assertEqual(largest_neg([-10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]), -10)

    def test_edge_case19(self):
        self.assertEqual(largest_neg([-10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]), -10)

    def test_edge_case20(self):
        self.assertEqual(largest_neg([-10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]), -10)

    def test_edge_case21(self):
        self.assertEqual(largest_neg([-10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]), -10)

    def test_edge_case22(self):
        self.assertEqual(largest_neg([-10,