import unittest
from mbpp_962_code import sum_Even

class TestSumEven(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_Even(2, 6), 12)
        self.assertEqual(sum_Even(6, 10), 20)
        self.assertEqual(sum_Even(10, 14), 22)

    def test_edge_case_even_start_end(self):
        self.assertEqual(sum_Even(0, 2), 0)
        self.assertEqual(sum_Even(2, 4), 4)
        self.assertEqual(sum_Even(4, 6), 12)

    def test_edge_case_odd_start_end(self):
        self.assertEqual(sum_Even(1, 3), 2)
        self.assertEqual(sum_Even(3, 5), 6)
        self.assertEqual(sum_Even(5, 7), 8)

    def test_boundary_case_zero(self):
        self.assertEqual(sum_Even(0, 0), 0)

    def test_boundary_case_one(self):
        self.assertEqual(sum_Even(1, 1), 0)
