import unittest
from mbpp_111_code import common_in_nested_lists

class TestCommonInNestedLists(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(common_in_nested_lists([[1, 2, 3], [2, 3, 4]]), [2, 3])
        self.assertEqual(common_in_nested_lists([[1, 2], [2, 3], [2, 4]]), [2])

    def test_edge_conditions(self):
        self.assertEqual(common_in_nested_lists([[], []]), [])
        self.assertEqual(common_in_nested_lists([[], [1, 2, 3]]), [])
        self.assertEqual(common_in_nested_lists([[1, 2, 3], []]), [])

    def test_boundary_conditions(self):
        self.assertEqual(common_in_nested_lists([[1], [1]]), [1])
        self.assertEqual(common_in_nested_lists([[1, 2, 3], [3, 2, 1]]), [1, 2, 3])
        self.assertEqual(common_in_nested_lists([[1, 2, 3], [4, 5, 6]]), [])

    def test_complex_cases(self):
        self.assertEqual(common_in_nested_lists([[1, 2, 3], [2, 3, 4], [3, 4, 5]]), [3])
        self.assertEqual(common_in_nested_lists([[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]), [3, 4])
