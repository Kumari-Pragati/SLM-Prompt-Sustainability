import unittest
from mbpp_162_code import sum_series

class TestSumSeries(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sum_series(3), 5)

    def test_edge_case(self):
        self.assertEqual(sum_series(1), 1)
        self.assertEqual(sum_series(0), 0)

    def test_edge_case_negative(self):
        self.assertEqual(sum_series(-1), 0)
        self.assertEqual(sum_series(-2), 0)

    def test_edge_case_zero(self):
        self.assertEqual(sum_series(0), 0)

    def test_edge_case_one(self):
        self.assertEqual(sum_series(1), 1)

    def test_edge_case_two(self):
        self.assertEqual(sum_series(2), 3)

    def test_edge_case_three(self):
        self.assertEqual(sum_series(3), 5)

    def test_edge_case_four(self):
        self.assertEqual(sum_series(4), 7)

    def test_edge_case_five(self):
        self.assertEqual(sum_series(5), 9)

    def test_edge_case_six(self):
        self.assertEqual(sum_series(6), 11)

    def test_edge_case_seven(self):
        self.assertEqual(sum_series(7), 13)

    def test_edge_case_eight(self):
        self.assertEqual(sum_series(8), 15)

    def test_edge_case_nine(self):
        self.assertEqual(sum_series(9), 17)

    def test_edge_case_ten(self):
        self.assertEqual(sum_series(10), 19)
