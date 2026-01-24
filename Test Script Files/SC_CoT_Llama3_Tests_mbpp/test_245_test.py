import unittest
from mbpp_245_code import max_sum

class TestMaxSum(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(max_sum([1, 2, 3, 4, 5], 5), 9)

    def test_edge_case(self):
        self.assertEqual(max_sum([-1, 0, 1], 3), 0)

    def test_edge_case_negative(self):
        self.assertEqual(max_sum([-1, -2, -3], 3), -1)

    def test_edge_case_zero(self):
        self.assertEqual(max_sum([0, 0, 0], 3), 0)

    def test_edge_case_one(self):
        self.assertEqual(max_sum([1, 1, 1], 3), 1)

    def test_edge_case_two(self):
        self.assertEqual(max_sum([1, 2, 3], 3), 3)

    def test_edge_case_three(self):
        self.assertEqual(max_sum([1, 2, 3, 4], 4), 4)

    def test_edge_case_four(self):
        self.assertEqual(max_sum([1, 2, 3, 4, 5], 5), 5)

    def test_edge_case_five(self):
        self.assertEqual(max_sum([1, 2, 3, 4, 5, 6], 6), 6)

    def test_edge_case_six(self):
        self.assertEqual(max_sum([1, 2, 3, 4, 5, 6, 7], 7), 7)

    def test_edge_case_seven(self):
        self.assertEqual(max_sum([1, 2, 3, 4, 5, 6, 7, 8], 8), 8)

    def test_edge_case_eight(self):
        self.assertEqual(max_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 9)

    def test_edge_case_nine(self):
        self.assertEqual(max_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 10)

    def test_edge_case_ten(self):
        self.assertEqual(max_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 11), 11)

    def test_edge_case_eleven(self):
        self.assertEqual(max_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 12), 12)

    def test_edge_case_twelve(self):
        self.assertEqual(max_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 13), 13)

    def test_edge_case_thirteen(self):
        self.assertEqual(max_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], 14), 14)

    def test_edge_case_fourteen(self):
        self.assertEqual(max_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 15), 15)

    def test_edge_case_fifteen(self):
        self.assertEqual(max_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 16), 16)

    def test_edge_case_sixteen(self):
        self.assertEqual(max_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 17), 17)

    def test_edge_case_seventeen(self):
        self.assertEqual(max_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], 18), 18)

    def test_edge_case_eighteen(self):
        self.assertEqual(max_sum([1, 2, 3, 4, 5, 6, 7, 8,