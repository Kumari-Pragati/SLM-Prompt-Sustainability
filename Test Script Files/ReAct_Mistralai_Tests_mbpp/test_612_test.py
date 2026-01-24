import unittest
from mbpp_612_code import zip
from 612_code import merge

class TestMergeFunction(unittest.TestCase):

    def test_empty_lists(self):
        self.assertEqual(merge([]), [])
        self.assertEqual(merge([[], []]), [[]])

    def test_single_list(self):
        self.assertEqual(merge([[1, 2, 3]]), [[1, 2, 3]])

    def test_two_lists(self):
        self.assertEqual(merge([[1, 2], [3, 4]]), [[1, 3], [2, 4]])

    def test_lists_of_different_lengths(self):
        self.assertEqual(merge([[1, 2], [3], [4, 5, 6]]), [[1, 3], [2, None, 4, 5, 6]])

    def test_lists_with_non_iterable_elements(self):
        self.assertRaises(TypeError, merge, [[1, 2], [3, 'x']])

    def test_lists_with_empty_elements(self):
        self.assertEqual(merge([[1, 2], [], [3, 4]]), [[1, None, 3], [2, None, 4]])
