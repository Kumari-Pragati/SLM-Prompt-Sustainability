import unittest
from mbpp_265_code import list_split

class TestListSplit(unittest.TestCase):

    def test_simple_step(self):
        self.assertListEqual(list_split([1, 2, 3, 4, 5], 1), [ [1], [2], [3], [4], [5] ])
        self.assertListEqual(list_split([1, 2, 3, 4, 5], 2), [ [1, 3], [2, 4], [5] ])
        self.assertListEqual(list_split([1, 2, 3, 4, 5], 3), [ [1, 4, 7], [2, 5], [3] ])

    def test_edge_cases(self):
        self.assertListEqual(list_split([], 2), [])
        self.assertListEqual(list_split([1], 2), [[]])
        self.assertListEqual(list_split([1, 2], 0), [])
        self.assertListEqual(list_split([1, 2], 5), [ [1], [2] ])
        self.assertListEqual(list_split([1, 2], -1), [ [2], [1] ])

    def test_complex_cases(self):
        self.assertListEqual(list_split([1, 2, 3, 4, 5, 6], 2), [ [1, 3], [2, 4], [5, 6] ])
        self.assertListEqual(list_split([1, 2, 3, 4, 5, 6], 3), [ [1, 4, 7], [2, 5, 8], [3, 6] ])
        self.assertListEqual(list_split([1, 2, 3, 4, 5, 6], 4), [ [1, 5], [2, 6], [3, 7], [4] ])
