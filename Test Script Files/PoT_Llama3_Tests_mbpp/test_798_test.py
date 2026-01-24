import unittest
from mbpp_798_code import _sum

class TestSumFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(_sum([1, 2, 3, 4, 5]), 15)

    def test_edge_case_empty_list(self):
        self.assertEqual(_sum([]), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(_sum([10]), 10)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(_sum([-1, -2, -3]), -6)

    def test_edge_case_mixed_numbers(self):
        self.assertEqual(_sum([1, -2, 3, -4, 5]), 3)

    def test_edge_case_large_numbers(self):
        self.assertEqual(_sum([100, 200, 300, 400, 500]), 1500)

    def test_edge_case_negative_and_positive_numbers(self):
        self.assertEqual(_sum([-1, 2, -3, 4, -5]), -3)
