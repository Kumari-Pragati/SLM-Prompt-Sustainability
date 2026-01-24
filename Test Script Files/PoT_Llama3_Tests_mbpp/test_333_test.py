import unittest
from mbpp_333_code import Sort

class TestSortFunction(unittest.TestCase):
    def test_typical_case(self):
        sub_li = [[1, 3], [2, 1], [3, 2]]
        self.assertEqual(Sort(sub_li), [[1, 3], [2, 1], [3, 2]])

    def test_edge_case_empty_list(self):
        sub_li = []
        self.assertEqual(Sort(sub_li), [])

    def test_edge_case_single_element_list(self):
        sub_li = [[1, 3]]
        self.assertEqual(Sort(sub_li), [[1, 3]])

    def test_edge_case_duplicates(self):
        sub_li = [[1, 3], [2, 1], [3, 2], [1, 3]]
        self.assertEqual(Sort(sub_li), [[1, 3], [1, 3], [2, 1], [3, 2]])

    def test_edge_case_negative_numbers(self):
        sub_li = [[-1, 3], [2, 1], [3, 2]]
        self.assertEqual(Sort(sub_li), [[-1, 3], [2, 1], [3, 2]])

    def test_edge_case_non_numeric_values(self):
        sub_li = [['a', 3], [2, 'b'], [3, 'c']]
        self.assertEqual(Sort(sub_li), [['a', 3], [2, 'b'], [3, 'c']])
