import unittest
from mbpp_696_code import zip_list

class TestZipList(unittest.TestCase):

    def test_empty_lists(self):
        self.assertListEqual(zip_list([], []), [])

    def test_single_element_lists(self):
        self.assertListEqual(zip_list([1], [2]), [3])
        self.assertListEqual(zip_list([2], [1]), [3])

    def test_lists_of_different_lengths(self):
        self.assertListEqual(zip_list([1, 2], [3, 4, 5]), [4, 6])
        self.assertListEqual(zip_list([1, 2, 3], [4]), [5, 6])

    def test_lists_with_none(self):
        self.assertListEqual(zip_list([None], [1, 2]), [None, 3])
        self.assertListEqual(zip_list([1, None], [2]), [3, None])

    def test_lists_with_numbers_and_strings(self):
        self.assertListEqual(zip_list([1, 'a'], [2, 'b']), ['1b', '2a'])

    def test_lists_with_lists(self):
        self.assertListEqual(zip_list([[1], [2]], [[3], [4]]), [[4], [5]])

    def test_lists_with_empty_elements(self):
        self.assertListEqual(zip_list([1, None], [2, None]), [2, None])
