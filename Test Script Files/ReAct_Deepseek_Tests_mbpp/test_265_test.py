import unittest
from mbpp_265_code import list_split

class TestListSplit(unittest.TestCase):

    def test_typical_case(self):
        S = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        step = 3
        expected_result = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        self.assertEqual(list_split(S, step), expected_result)

    def test_edge_case_step_one(self):
        S = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        step = 1
        expected_result = [[1], [2], [3], [4], [5], [6], [7], [8], [9]]
        self.assertEqual(list_split(S, step), expected_result)

    def test_edge_case_step_equal_to_list_length(self):
        S = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        step = len(S)
        expected_result = [[1, 2, 3, 4, 5, 6, 7, 8, 9]]
        self.assertEqual(list_split(S, step), expected_result)

    def test_edge_case_step_greater_than_list_length(self):
        S = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        step = len(S) + 1
        expected_result = []
        self.assertEqual(list_split(S, step), expected_result)

    def test_edge_case_empty_list(self):
        S = []
        step = 3
        expected_result = []
        self.assertEqual(list_split(S, step), expected_result)
