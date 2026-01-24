import unittest
from mbpp_805_code import max_sum_list

class TestMaxSumList(unittest.TestCase):
    def test_typical_use_case(self):
        lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(max_sum_list(lists), [7, 8, 9])

    def test_edge_case_empty_list(self):
        lists = []
        self.assertIsNone(max_sum_list(lists))

    def test_boundary_case_single_list(self):
        lists = [[1, 2, 3]]
        self.assertEqual(max_sum_list(lists), [1, 2, 3])

    def test_boundary_case_single_element_in_list(self):
        lists = [[1], [2], [3]]
        self.assertEqual(max_sum_list(lists), [3])

    def test_error_handling_non_list_element(self):
        lists = [[1, 2, 3], 'abc', [4, 5, 6]]
        with self.assertRaises(TypeError):
            max_sum_list(lists)
