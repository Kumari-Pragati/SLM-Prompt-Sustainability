import unittest
from mbpp_675_code import sum_nums

class TestSumNums(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sum_nums(5, 7, 10, 20), 20)

    def test_edge_case(self):
        self.assertEqual(sum_nums(5, 7, 5, 15), 12)

    def test_edge_case2(self):
        self.assertEqual(sum_nums(5, 7, 15, 20), 12)

    def test_edge_case3(self):
        self.assertEqual(sum_nums(5, 7, 20, 25), 12)

    def test_edge_case4(self):
        self.assertEqual(sum_nums(5, 7, 25, 30), 12)

    def test_edge_case5(self):
        self.assertEqual(sum_nums(5, 7, 30, 35), 12)

    def test_edge_case6(self):
        self.assertEqual(sum_nums(5, 7, 35, 40), 12)

    def test_edge_case7(self):
        self.assertEqual(sum_nums(5, 7, 40, 45), 12)

    def test_edge_case8(self):
        self.assertEqual(sum_nums(5, 7, 45, 50), 12)

    def test_edge_case9(self):
        self.assertEqual(sum_nums(5, 7, 50, 55), 12)

    def test_edge_case10(self):
        self.assertEqual(sum_nums(5, 7, 55, 60), 12)

    def test_typical_case2(self):
        self.assertEqual(sum_nums(5, 7, 1, 10), 12)

    def test_typical_case3(self):
        self.assertEqual(sum_nums(5, 7, 10, 20), 12)

    def test_typical_case4(self):
        self.assertEqual(sum_nums(5, 7, 20, 30), 12)

    def test_typical_case5(self):
        self.assertEqual(sum_nums(5, 7, 30, 40), 12)

    def test_typical_case6(self):
        self.assertEqual(sum_nums(5, 7, 40, 50), 12)

    def test_typical_case7(self):
        self.assertEqual(sum_nums(5, 7, 50, 60), 12)

    def test_typical_case8(self):
        self.assertEqual(sum_nums(5, 7, 60, 70), 12)

    def test_typical_case9(self):
        self.assertEqual(sum_nums(5, 7, 70, 80), 12)

    def test_typical_case10(self):
        self.assertEqual(sum_nums(5, 7, 80, 90), 12)
