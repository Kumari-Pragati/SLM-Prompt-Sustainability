import unittest
from mbpp_265_code import list_split

class TestListSplit(unittest.TestCase):
    def test_empty_list(self):
        self.assertListEqual(list_split([], 3), [[]])

    def test_single_element_list(self):
        self.assertListEqual(list_split([1], 3), [[]])
        self.assertListEqual(list_split([1], 1), [ [1] ])
        self.assertListEqual(list_split([1], 2), [ [1], [] ])

    def test_simple_list(self):
        self.assertListEqual(list_split([1, 2, 3, 4], 2), [ [1, 3], [2, 4] ])
        self.assertListEqual(list_split([1, 2, 3, 4], 1), [ [1], [2], [3], [4] ])
        self.assertListEqual(list_split([1, 2, 3, 4], 4), [ [1], [2], [3], [4] ])

    def test_step_larger_than_list_length(self):
        self.assertListEqual(list_split([1, 2, 3], 5), [ [1, 2, 3] ])

    def test_negative_step(self):
        self.assertRaises(ValueError, lambda: list_split([1, 2, 3], -1))

    def test_step_zero(self):
        self.assertRaises(ValueError, lambda: list_split([1, 2, 3], 0))
