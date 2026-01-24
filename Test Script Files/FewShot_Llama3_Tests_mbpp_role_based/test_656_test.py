import unittest
from mbpp_656_code import find_Min_Sum

class TestFindMinSum(unittest.TestCase):
    def test_typical_use_case(self):
        a = [1, 3, 5, 7, 9]
        b = [2, 4, 6, 8, 10]
        n = 5
        self.assertEqual(find_Min_Sum(a, b, n), 10)

    def test_edge_case_empty_list(self):
        a = []
        b = []
        n = 0
        self.assertEqual(find_Min_Sum(a, b, n), 0)

    def test_edge_case_single_element_list(self):
        a = [1]
        b = [2]
        n = 1
        self.assertEqual(find_Min_Sum(a, b, n), 1)

    def test_edge_case_negative_numbers(self):
        a = [-1, -3, -5, -7, -9]
        b = [-2, -4, -6, -8, -10]
        n = 5
        self.assertEqual(find_Min_Sum(a, b, n), 10)

    def test_edge_case_zero(self):
        a = [0, 0, 0, 0, 0]
        b = [0, 0, 0, 0, 0]
        n = 5
        self.assertEqual(find_Min_Sum(a, b, n), 0)
