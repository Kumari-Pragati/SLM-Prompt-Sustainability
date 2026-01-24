import unittest
from mbpp_587_code import list_tuple

class TestListTuple(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsInstance(list_tuple([]), tuple)

    def test_single_element_list(self):
        self.assertListEqual(list_tuple([1]), (1,))

    def test_multiple_elements_list(self):
        self.assertListEqual(list_tuple([1, 2, 3]), (1, 2, 3))

    def test_list_with_different_types(self):
        self.assertRaises(TypeError, list_tuple, [1, 'a', 3.14])

    def test_list_with_duplicate_elements(self):
        self.assertListEqual(list_tuple([1, 1, 2, 2, 3]), (1, 1, 2, 2, 3))

    def test_list_with_none(self):
        self.assertListEqual(list_tuple([None]), (None,))
