import unittest
from mbpp_106_code import add_lists

class TestAddLists(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(add_lists([], (1, 2, 3)), (1, 2, 3))

    def test_non_empty_list(self):
        self.assertEqual(add_lists([1, 2, 3], (4, 5, 6)), (4, 5, 6, 1, 2, 3))

    def test_empty_tuple(self):
        self.assertEqual(add_lists([1, 2, 3], ()), (1, 2, 3))

    def test_non_empty_tuple(self):
        self.assertEqual(add_lists([1, 2, 3], (4, 5, 6)), (4, 5, 6, 1, 2, 3))

    def test_mixed_input_types(self):
        self.assertEqual(add_lists([1, 2, 3], (4, 5)), (4, 5, 1, 2, 3))
