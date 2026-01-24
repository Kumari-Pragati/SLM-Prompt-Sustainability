import unittest
from mbpp_111_code import common_in_nested_lists

class TestCommonInNestedLists(unittest.TestCase):

    def test_common_in_nested_lists(self):
        self.assertEqual(common_in_nested_lists([[1, 2, 3], [2, 3, 4], [3, 4, 5]]), [3])
        self.assertEqual(common_in_nested_lists([[1, 2, 3], [2, 3, 4], [3, 4, 5, 6]]), [3, 4])
        self.assertEqual(common_in_nested_lists([[1, 2, 3], [2, 3, 4], [3, 4, 5, 6, 7]]), [3, 4, 5, 6])
        self.assertEqual(common_in_nested_lists([[1, 2, 3], [2, 3, 4], [3, 4, 5, 6, 7, 8]]), [3, 4, 5, 6, 7, 8])
        self.assertEqual(common_in_nested_lists([[1, 2, 3], [2, 3, 4], [3, 4, 5, 6, 7, 8, 9]]), [3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(common_in_nested_lists([[1, 2, 3], [2, 3, 4], [3, 4, 5, 6, 7, 8, 9, 10]]), [3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(common_in_nested_lists([[1, 2, 3], [2, 3, 4], [3, 4, 5, 6, 7, 8, 9, 10, 11]]), [3, 4, 5, 6, 7, 8, 9, 10, 11])
        self.assertEqual(common_in_nested_lists([[1, 2, 3], [2, 3, 4], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]), [3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        self.assertEqual(common_in_nested_lists([[1, 2, 3], [2, 3, 4], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]]), [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
        self.assertEqual(common_in_nested_lists([[1, 2, 3], [2, 3, 4], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]]), [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
        self.assertEqual(common_in_nested_lists([[1, 2, 3], [2, 3, 4], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]]), [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        self.assertEqual(common_in_nested_lists([[1, 2, 3], [2, 3, 4], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]]), [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
        self.assertEqual(common_in_nested_lists([[1, 2, 3], [2, 3, 4], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]]), [3, 4, 5, 6