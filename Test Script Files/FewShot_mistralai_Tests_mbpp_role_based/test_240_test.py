import unittest
from mbpp_240_code import replace_list

class TestReplaceList(unittest.TestCase):
    def test_replace_empty_list(self):
        self.assertListEqual(replace_list([], [1, 2, 3]), [1, 2, 3])

    def test_replace_single_element_list(self):
        self.assertListEqual(replace_list([4], [1, 2, 3]), [1, 2, 3])

    def test_replace_list_with_same_length(self):
        self.assertListEqual(replace_list([1, 2, 3], [4, 5, 6]), [4, 5, 6])

    def test_replace_list_with_shorter_length(self):
        self.assertListEqual(replace_list([1, 2, 3], [4]), [4])

    def test_replace_list_with_longer_length(self):
        self.assertListEqual(replace_list([1, 2, 3], [4, 5, 6, 7]), [4, 5, 6])
