import unittest
from mbpp_106_code import add_lists

class TestAddLists(unittest.TestCase):
    def test_normal_input(self):
        self.assertListEqual(add_lists([1, 2, 3], (4, 5, 6)), [1, 2, 3, 4, 5, 6])

    def test_empty_input(self):
        self.assertListEqual(add_lists([], (1, 2, 3)), [1, 2, 3])
        self.assertListEqual(add_lists((1, 2, 3), []), [1, 2, 3])

    def test_single_input(self):
        self.assertListEqual(add_lists([1, 2, 3], (1, 2, 3)), [1, 2, 3, 1, 2, 3])
        self.assertListEqual(add_lists((1, 2, 3), [1, 2, 3]), [1, 2, 3, 1, 2, 3])

    def test_mixed_types(self):
        self.assertRaises(TypeError, add_lists, [1, 2, 3], (1, '2', 3))

    def test_list_with_tuple(self):
        self.assertListEqual(add_lists([(1, 2, 3)], [4, 5, 6]), [(1, 2, 3), 4, 5, 6])
        self.assertListEqual(add_lists([(1, 2, 3)], (4, 5, 6)), [(1, 2, 3), 4, 5, 6])
