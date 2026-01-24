import unittest
from mbpp_859_code import sub_lists

class TestSubLists(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sub_lists([]), [])

    def test_single_element_list(self):
        self.assertEqual(sub_lists([1]), [[[]], [[1]]])

    def test_two_element_list(self):
        self.assertEqual(sub_lists([1, 2]), [[[], [1], [2], [1, 2]], [[1], [2]]])

    def test_three_element_list(self):
        self.assertEqual(sub_lists([1, 2, 3]), [[[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]], [[1], [2], [3]]))

    def test_four_element_list(self):
        self.assertEqual(sub_lists([1, 2, 3, 4]), [[[], [1], [2], [3], [4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4], [1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4]], [[1], [2], [3], [4]]))

    def test_list_with_duplicates(self):
        self.assertEqual(sub_lists([1, 2, 2, 3, 3, 3]), [[[], [1], [2], [2, 2], [3], [2, 3], [3, 3], [1, 2], [1, 2, 2], [1, 3], [1, 3, 3], [2, 3, 3], [1, 2, 3], [2, 2, 3], [1, 2, 2, 3], [1, 2, 3, 3], [2, 2, 3, 3], [1, 2, 2, 3, 3]], [[1], [2], [3]]))

    def test_list_with_duplicates_and_empty_sublists(self):
        self.assertEqual(sub_lists([1, 2, 2, 3, 3, 3, []]), [[[], [1], [2], [2, 2], [3], [2, 3], [3, 3], [1, 2], [1, 2, 2], [1, 3], [1, 3, 3], [2, 3, 3], [1, 2, 3], [2, 2, 3], [1, 2, 2, 3], [1, 2, 3, 3], [2, 2, 3, 3], [1, 2, 2, 3, 3], [1, 2, 3, 3, []], [2, 2, 3, 3, []], [1, 2, 2, 3, 3, []], [1, 2, 3, 3, [], []], [2, 2, 3, 3, [], []], [1, 2, 2, 3, 3, [], []]], [[1], [2], [3]]))
