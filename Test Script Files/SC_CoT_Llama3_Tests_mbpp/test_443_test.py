import unittest
from mbpp_443_code import largest_neg

class TestLargestNeg(unittest.TestCase):

    def test_typical(self):
        self.assertEqual(largest_neg([-10, -5, 0, 5, 10]), -10)

    def test_edge_case(self):
        self.assertEqual(largest_neg([-10, -5, -3, -2, -1]), -10)

    def test_edge_case2(self):
        self.assertEqual(largest_neg([-10, -5, 0, 5, 10, 20]), -10)

    def test_edge_case3(self):
        self.assertEqual(largest_neg([-10, -5, 0, 5, 10, 20, 30]), -10)

    def test_edge_case4(self):
        self.assertEqual(largest_neg([-10, -5, 0, 5, 10, 20, 30, 40]), -10)

    def test_edge_case5(self):
        self.assertEqual(largest_neg([-10, -5, 0, 5, 10, 20, 30, 40, 50]), -10)

    def test_edge_case6(self):
        self.assertEqual(largest_neg([-10, -5, 0, 5, 10, 20, 30, 40, 50, 60]), -10)

    def test_edge_case7(self):
        self.assertEqual(largest_neg([-10, -5, 0, 5, 10, 20, 30, 40, 50, 60, 70]), -10)

    def test_edge_case8(self):
        self.assertEqual(largest_neg([-10, -5, 0, 5, 10, 20, 30, 40, 50, 60, 70, 80]), -10)

    def test_edge_case9(self):
        self.assertEqual(largest_neg([-10, -5, 0, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90]), -10)

    def test_edge_case10(self):
        self.assertEqual(largest_neg([-10, -5, 0, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]), -10)

    def test_edge_case11(self):
        self.assertEqual(largest_neg([-10, -5, 0, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]), -10)

    def test_edge_case12(self):
        self.assertEqual(largest_neg([-10, -5, 0, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]), -10)

    def test_edge_case13(self):
        self.assertEqual(largest_neg([-10, -5, 0, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]), -10)

    def test_edge_case14(self):
        self.assertEqual(largest_neg([-10, -5, 0, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140]), -10)

    def test_edge_case15(self):
        self.assertEqual(largest_neg([-10, -5, 0, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]), -10)

    def test_edge_case16(self):
        self.assertEqual(largest_neg([-10, -5, 0, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]), -10)

    def test_edge_case17(self):
        self.assertEqual(largest_neg([-10, -5, 0, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170]), -10)

    def test_edge_case18(self):
        self.assertEqual(largest_neg([-10, -5, 0,