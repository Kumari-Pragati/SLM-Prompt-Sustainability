import unittest
from mbpp_265_code import list_split

class TestListSplit(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(list_split([1, 2, 3, 4, 5], 1), [
            [1], [2], [3], [4], [5]
        ])
        self.assertEqual(list_split([1, 2, 3, 4, 5], 2), [
            [1, 3], [2, 4], [5]
        ])
        self.assertEqual(list_split([1, 2, 3, 4, 5], 3), [
            [1, 4], [2, 5], [3]
        ])
        self.assertEqual(list_split([1, 2, 3, 4, 5], 4), [
            [1, 5], [2, 6], [3, 7], [4]
        ])

    def test_edge_and_boundary_cases(self):
        self.assertEqual(list_split([], 1), [])
        self.assertEqual(list_split([1], 1), [[1]])
        self.assertEqual(list_split([1, 2], 1), [[1], [2]])
        self.assertEqual(list_split([1, 2], 2), [[1], [2]])
        self.assertEqual(list_split([1, 2], 3), [[1], [2]])
        self.assertEqual(list_split([1, 2], 4), [[1], [2]])
        self.assertEqual(list_split([1, 2], 5), [[1], [2]])
        self.assertEqual(list_split([1, 2], 0), [])
        self.assertEqual(list_split([1, 2], -1), [])
        self.assertEqual(list_split([1, 2], -2), [])
