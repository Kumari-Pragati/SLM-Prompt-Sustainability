import unittest
from mbpp_265_code import list_split

class TestListSplit(unittest.TestCase):
    def test_typical_use_case(self):
        S = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        step = 3
        expected_output = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(list_split(S, step), expected_output)

    def test_edge_condition(self):
        S = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        step = 1
        expected_output = [[1], [2], [3], [4], [5], [6], [7], [8], [9]]
        self.assertEqual(list_split(S, step), expected_output)

    def test_boundary_condition(self):
        S = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        step = 10
        expected_output = [[1, 2, 3, 4, 5, 6, 7, 8, 9]]
        self.assertEqual(list_split(S, step), expected_output)

    def test_invalid_input(self):
        S = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        step = 'a'
        with self.assertRaises(TypeError):
            list_split(S, step)
