import unittest
from mbpp_106_code import add_lists

class TestAddLists(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(add_lists([1, 2, 3], (4, 5, 6)), (4, 5, 6, 1, 2, 3))

    def test_empty_list(self):
        self.assertEqual(add_lists([], (1, 2, 3)), (1, 2, 3))

    def test_empty_tuple(self):
        self.assertEqual(add_lists([1, 2, 3], ()), (1, 2, 3))

    def test_single_element(self):
        self.assertEqual(add_lists([1], (2,)), (2, 1))

    def test_edge_case(self):
        self.assertEqual(add_lists([1, 2, 3, 4, 5], (1, 2, 3, 4, 5)), (1, 2, 3, 4, 5, 1, 2, 3, 4, 5))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            add_lists("test", (1, 2, 3))
