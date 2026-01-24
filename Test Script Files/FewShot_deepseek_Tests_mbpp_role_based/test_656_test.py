import unittest
from mbpp_656_code import find_Min_Sum

class TestFindMinSum(unittest.TestCase):
    def test_typical_use_case(self):
        a = [1, 2, 3, 4, 5]
        b = [5, 4, 3, 2, 1]
        n = 5
        self.assertEqual(find_Min_Sum(a, b, n), 0)

    def test_edge_case_with_single_element(self):
        a = [1]
        b = [2]
        n = 1
        self.assertEqual(find_Min_Sum(a, b, n), 1)

    def test_boundary_case_with_empty_lists(self):
        a = []
        b = []
        n = 0
        self.assertEqual(find_Min_Sum(a, b, n), 0)

    def test_boundary_case_with_one_empty_list(self):
        a = [1, 2, 3]
        b = []
        n = 3
        self.assertRaises(IndexError, find_Min_Sum, a, b, n)

    def test_invalid_input_with_non_list_a(self):
        a = "not a list"
        b = [1, 2, 3]
        n = 3
        self.assertRaises(TypeError, find_Min_Sum, a, b, n)

    def test_invalid_input_with_non_list_b(self):
        a = [1, 2, 3]
        b = "not a list"
        n = 3
        self.assertRaises(TypeError, find_Min_Sum, a, b, n)

    def test_invalid_input_with_negative_n(self):
        a = [1, 2, 3]
        b = [4, 5, 6]
        n = -1
        self.assertRaises(ValueError, find_Min_Sum, a, b, n)
