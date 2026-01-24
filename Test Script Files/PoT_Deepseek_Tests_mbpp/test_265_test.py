import unittest
from mbpp_265_code import list_split

class TestListSplit(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(list_split([1, 2, 3, 4, 5, 6, 7, 8, 9], 3),
                         [[1, 4, 7], [2, 5, 8], [3, 6, 9]])

    def test_edge_case_step_one(self):
        self.assertEqual(list_split([1, 2, 3, 4, 5, 6, 7, 8, 9], 1),
                         [[1], [2], [3], [4], [5], [6], [7], [8], [9]])

    def test_boundary_case_step_zero(self):
        with self.assertRaises(ValueError):
            list_split([1, 2, 3, 4, 5, 6, 7, 8, 9], 0)

    def test_corner_case_empty_list(self):
        self.assertEqual(list_split([], 3), [[]]*3)

    def test_corner_case_step_greater_than_list_length(self):
        self.assertEqual(list_split([1, 2, 3, 4, 5, 6, 7, 8, 9], 10),
                         [[1, 2, 3, 4, 5, 6, 7, 8, 9]])
