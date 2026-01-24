import unittest
from mbpp_612_code import merge

class TestMergeFunction(unittest.TestCase):

    def test_merge_function(self):
        self.assertEqual(merge([[1, 2], [3, 4]]), [[1, 3], [2, 4]])
        self.assertEqual(merge([[1, 2, 3], [4, 5, 6]]), [[1, 4], [2, 5], [3, 6]])
        self.assertEqual(merge([[1, 2, 3, 4], [5, 6, 7, 8]]), [[1, 5], [2, 6], [3, 7], [4, 8]])
        self.assertEqual(merge([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]), [[1, 6], [2, 7], [3, 8], [4, 9], [5, 10]])
        self.assertEqual(merge([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]]), [[1, 7], [2, 8], [3, 9], [4, 10], [5, 11], [6, 12]])

    def test_merge_function_empty_list(self):
        self.assertEqual(merge([]), [])

    def test_merge_function_single_list(self):
        self.assertEqual(merge([[1, 2, 3, 4, 5]]), [[1], [2], [3], [4], [5]])
