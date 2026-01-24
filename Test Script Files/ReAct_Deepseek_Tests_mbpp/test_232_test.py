import unittest
from mbpp_232_code import larg_nnum

class TestLargNnum(unittest.TestCase):

    def test_typical_case(self):
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        n = 5
        result = larg_nnum(list1, n)
        self.assertEqual(result, [9, 8, 7, 6, 5])

    def test_edge_case_n_equals_zero(self):
        list1 = [1, 2, 3, 4, 5]
        n = 0
        result = larg_nnum(list1, n)
        self.assertEqual(result, [])

    def test_edge_case_n_greater_than_list_length(self):
        list1 = [1, 2, 3, 4, 5]
        n = 10
        result = larg_nnum(list1, n)
        self.assertEqual(result, list1)

    def test_edge_case_empty_list(self):
        list1 = []
        n = 5
        result = larg_nnum(list1, n)
        self.assertEqual(result, [])

    def test_edge_case_negative_numbers(self):
        list1 = [-1, -2, -3, -4, -5]
        n = 3
        result = larg_nnum(list1, n)
        self.assertEqual(result, [-1, -2, -3])

    def test_edge_case_duplicate_numbers(self):
        list1 = [5, 5, 4, 4, 3, 2, 1]
        n = 3
        result = larg_nnum(list1, n)
        self.assertEqual(result, [5, 5, 4])
