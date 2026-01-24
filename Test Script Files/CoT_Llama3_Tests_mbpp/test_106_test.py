import unittest
from mbpp_106_code import add_lists

class TestAddLists(unittest.TestCase):

    def test_add_lists_typical(self):
        self.assertEqual(add_lists([1, 2, 3], (4, 5, 6)), (4, 5, 6, 1, 2, 3))

    def test_add_lists_empty_list(self):
        self.assertEqual(add_lists([], (1, 2, 3)), (1, 2, 3))

    def test_add_lists_empty_tuple(self):
        self.assertEqual(add_lists([1, 2, 3], ()), (1, 2, 3))

    def test_add_lists_single_element(self):
        self.assertEqual(add_lists([1], (2, 3)), (2, 3, 1))

    def test_add_lists_multiple_elements(self):
        self.assertEqual(add_lists([1, 2, 3, 4, 5], (6, 7, 8, 9, 10)), (6, 7, 8, 9, 10, 1, 2, 3, 4, 5))

    def test_add_lists_mixed_types(self):
        self.assertEqual(add_lists([1, 'a', 3.5], (4, 'b', 5.6)), (4, 'b', 5.6, 1, 'a', 3.5))
