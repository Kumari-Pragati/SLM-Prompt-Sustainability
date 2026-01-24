import unittest
from mbpp_111_code import common_in_nested_lists

class TestCommonInNestedLists(unittest.TestCase):

    def test_common_in_nested_lists(self):
        self.assertEqual(common_in_nested_lists([[1, 2, 3], [2, 3, 4], [3, 4, 5]]), [3])
        self.assertEqual(common_in_nested_lists([[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]), [3, 4])
        self.assertEqual(common_in_nested_lists([[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7]]), [3, 4, 5])
        self.assertEqual(common_in_nested_lists([[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8]]), [3, 4, 5, 6])
        self.assertEqual(common_in_nested_lists([[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9]]), [3, 4, 5, 6, 7])
        self.assertEqual(common_in_nested_lists([[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10]]), [3, 4, 5, 6, 7, 8])
