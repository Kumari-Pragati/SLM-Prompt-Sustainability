import unittest
from mbpp_106_code import add_lists

class TestAddLists(unittest.TestCase):

    def test_add_lists_with_empty_list(self):
        self.assertListEqual(add_lists([], (1, 2, 3)), [1, 2, 3])

    def test_add_lists_with_empty_tuple(self):
        self.assertListEqual(add_lists((1,), []), [1])

    def test_add_lists_with_single_element_list(self):
        self.assertListEqual(add_lists([1], (2, 3)), [1, 2, 3])

    def test_add_lists_with_single_element_tuple(self):
        self.assertListEqual(add_lists([1, 2], (3,)), [1, 2, 3])

    def test_add_lists_with_multiple_elements(self):
        self.assertListEqual(add_lists([1, 2, 3], (4, 5, 6)), [1, 2, 3, 4, 5, 6])

    def test_add_lists_with_mixed_types(self):
        self.assertRaises(TypeError, add_lists, [1, 2, 3], (1, 2, "3"))

    def test_add_lists_with_list_as_tuple(self):
        self.assertListEqual(add_lists([(1, 2)], [3, 4]), [(1, 2), 3, 4])
