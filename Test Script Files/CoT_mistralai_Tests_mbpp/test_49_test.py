import unittest
from mbpp_49_code import specified_element

class TestSpecifiedElement(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual([], specified_element([], 0))

    def test_single_list(self):
        self.assertListEqual([1], specified_element([[1]], 0))

    def test_multiple_lists(self):
        self.assertListEqual([1, 2, 3], specified_element([[1], [2], [3]], 0))

    def test_negative_index(self):
        self.assertRaises(IndexError, specified_element, [[1], [2], [3]], -1)

    def test_index_greater_than_length(self):
        self.assertRaises(IndexError, specified_element, [[1], [2], [3]], 3)

    def test_non_list_input(self):
        self.assertRaises(TypeError, specified_element, 'not a list', 0)
