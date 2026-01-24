import unittest
from mbpp_111_code import common_in_nested_lists

class TestCommonInNestedLists(unittest.TestCase):

    def test_normal_case(self):
        self.assertListEqual(common_in_nested_lists([[1, 2, 3], [4, 2, 1], [3, 4, 5]]), [1, 2, 3])
        self.assertListEqual(common_in_nested_lists([{'a': 1}, {'a': 2}, {'a': 3}]), [1, 2, 3])

    def test_edge_cases(self):
        self.assertListEqual(common_in_nested_lists([[]]), [])
        self.assertListEqual(common_in_nested_lists([[1]]), [1])
        self.assertListEqual(common_in_nested_lists([[1], [1]]), [1])
        self.assertListEqual(common_in_nested_lists([[1, 2], [2, 1]]), [1, 2])
        self.assertListEqual(common_in_nested_lists([[1], [2]]), [])

    def test_boundary_cases(self):
        self.assertListEqual(common_in_nested_lists([[-1], [0], [1]]), [0])
        self.assertListEqual(common_in_nested_lists([[0], [1], [2], [3]]), [0])
        self.assertListEqual(common_in_nested_lists([[0], [1], [2], [3], [4]]), [0])

    def test_special_cases(self):
        self.assertListEqual(common_in_nested_lists([[1, 2, 3], [1, 2, 4], [1, 3, 4]]), [1, 2, 3])
        self.assertListEqual(common_in_nested_lists([[1, 2, 3], [1, 2, 4], [1, 3, 4], [1, 2, 5]]), [1, 2, 3])
        self.assertListEqual(common_in_nested_lists([[1, 2, 3], [1, 2, 4], [1, 3, 4], [1, 2, 5], [1, 2, 6]]), [1, 2, 3])
