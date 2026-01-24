import unittest
from mbpp_106_code import add_lists

class TestAddLists(unittest.TestCase):
    def test_add_empty_list_and_tuple(self):
        self.assertEqual(add_lists([], (1, 2, 3)), (1, 2, 3))

    def test_add_list_and_empty_tuple(self):
        self.assertEqual(add_lists([1, 2, 3], ()), (1, 2, 3))

    def test_add_list_and_tuple(self):
        self.assertEqual(add_lists([1, 2, 3], (4, 5, 6)), (1, 2, 3, 4, 5, 6))

    def test_add_list_and_list(self):
        self.assertEqual(add_lists([1, 2, 3], [4, 5, 6]), [1, 2, 3, 4, 5, 6])

    def test_add_list_and_set(self):
        with self.assertRaises(TypeError):
            add_lists([1, 2, 3], {4, 5, 6})

    def test_add_set_and_tuple(self):
        with self.assertRaises(TypeError):
            add_lists({1, 2, 3}, (4, 5, 6))
