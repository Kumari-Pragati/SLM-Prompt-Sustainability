import unittest
from mbpp_798_code import _sum

class TestSumFunction(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(_sum([1, 2, 3, 4, 5]), 15)

    def test_edge_case_empty_list(self):
        self.assertEqual(_sum([]), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(_sum([1]), 1)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(_sum([1, -2, 3, -4, 5]), 6)

    def test_corner_case_large_numbers(self):
        self.assertEqual(_sum([1000000001, 1000000002, 1000000003]), 3000000006)
