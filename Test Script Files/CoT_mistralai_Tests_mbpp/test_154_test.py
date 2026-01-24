import unittest
from mbpp_154_code import specified_element

class TestSpecifiedElement(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual([], specified_element([], 0))

    def test_single_element_list(self):
        self.assertListEqual([1], specified_element([(1,)], 0))

    def test_multiple_elements_list(self):
        self.assertListEqual([1, 2, 3], specified_element([(1,), (2,), (3,)], 1))

    def test_negative_index(self):
        self.assertListEqual([], specified_element([(1,), (2,), (3,)], -1))

    def test_index_greater_than_length(self):
        self.assertListEqual([], specified_element([(1,), (2,), (3,)], 4))

    def test_list_with_non_tuple_elements(self):
        self.assertRaises(TypeError, specified_element, [1, 2, 3], 0)
