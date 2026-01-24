import unittest
from mbpp_265_code import list_split

class TestListSplit(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(list_split([1, 2, 3, 4, 5], 2), [
            [1, 3],
            [2, 4],
            [5]
        ])

    def test_edge_case_step_1(self):
        self.assertEqual(list_split([1, 2, 3, 4, 5], 1), [
            [1],
            [2],
            [3],
            [4],
            [5]
        ])

    def test_edge_case_step_len(self):
        self.assertEqual(list_split([1, 2, 3, 4, 5], 5), [
            [1],
            [2],
            [3],
            [4],
            [5]
        ])

    def test_edge_case_empty_list(self):
        self.assertEqual(list_split([], 2), [])

    def test_edge_case_step_0(self):
        self.assertRaises(ValueError, lambda: list_split([1], 0))

    def test_corner_case_negative_step(self):
        self.assertRaises(ValueError, lambda: list_split([1, 2, 3], -1))
