import unittest
from mbpp_10_code import small_nnum

class TestSmallNNum(unittest.TestCase):

    def test_typical_case(self):
        list1 = [3, 1, 2, 5, 4]
        n = 3
        result = small_nnum(list1, n)
        self.assertEqual(result, [1, 2, 3])

    def test_edge_case_n_equals_zero(self):
        list1 = [3, 1, 2, 5, 4]
        n = 0
        result = small_nnum(list1, n)
        self.assertEqual(result, [])

    def test_edge_case_n_greater_than_list_length(self):
        list1 = [3, 1, 2, 5, 4]
        n = 10
        result = small_nnum(list1, n)
        self.assertEqual(result, sorted(list1))

    def test_edge_case_empty_list(self):
        list1 = []
        n = 3
        result = small_nnum(list1, n)
        self.assertEqual(result, [])

    def test_edge_case_negative_numbers(self):
        list1 = [-3, -1, -2, -5, -4]
        n = 3
        result = small_nnum(list1, n)
        self.assertEqual(result, [-5, -4, -3])

    def test_edge_case_duplicate_numbers(self):
        list1 = [3, 1, 2, 2, 4]
        n = 3
        result = small_nnum(list1, n)
        self.assertEqual(result, [1, 2, 2])
