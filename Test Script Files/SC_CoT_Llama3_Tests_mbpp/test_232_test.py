import unittest
from mbpp_232_code import larg_nnum

class TestLargNnum(unittest.TestCase):
    def test_typical_input(self):
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = 3
        result = larg_nnum(list1, n)
        self.assertEqual(result, [9, 8, 7])

    def test_edge_case_n_equal_to_length(self):
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = 10
        result = larg_nnum(list1, n)
        self.assertEqual(result, list1)

    def test_edge_case_n_greater_than_length(self):
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = 20
        result = larg_nnum(list1, n)
        self.assertEqual(result, list1)

    def test_edge_case_empty_list(self):
        list1 = []
        n = 3
        result = larg_nnum(list1, n)
        self.assertEqual(result, [])

    def test_edge_case_n_zero(self):
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = 0
        result = larg_nnum(list1, n)
        self.assertEqual(result, [])

    def test_edge_case_n_negative(self):
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = -3
        result = larg_nnum(list1, n)
        self.assertEqual(result, [])
