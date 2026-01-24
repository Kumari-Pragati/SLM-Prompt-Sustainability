import unittest
from mbpp_240_code import replace_list

class TestReplaceList(unittest.TestCase):

    def test_empty_list1(self):
        self.assertListEqual(replace_list([], ['a']), ['a'])

    def test_single_element_list1(self):
        self.assertListEqual(replace_list([1], [2, 3]), [2, 3])

    def test_multiple_elements_list1(self):
        self.assertListEqual(replace_list([1, 2, 3], [4, 5, 6]), [4, 5, 6])

    def test_list1_with_none(self):
        self.assertListEqual(replace_list([None], ['a', 'b']), ['a', 'b'])

    def test_list2_with_none(self):
        self.assertListEqual(replace_list([1, 2, 3], [None]), [None])

    def test_list1_with_empty_list2(self):
        self.assertListEqual(replace_list([1, 2, 3], []), [])

    def test_list2_with_single_element(self):
        self.assertListEqual(replace_list([1, 2, 3], [4]), [4])

    def test_list2_with_multiple_elements(self):
        self.assertListEqual(replace_list([1, 2, 3], [4, 5, 6]), [4, 5, 6])

    def test_list1_with_negative_index(self):
        self.assertRaises(IndexError, lambda: replace_list([1, 2, 3], [4, 5, 6]), -1)

    def test_list2_with_negative_index(self):
        self.assertRaises(IndexError, lambda: replace_list([1, 2, 3], [-1]), -1)
