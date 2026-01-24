import unittest
from mbpp_106_code import add_lists

class TestAddLists(unittest.TestCase):

    def test_simple_list_and_tuple(self):
        self.assertEqual(add_lists([1, 2, 3], (4, 5, 6)), (4, 5, 6, 1, 2, 3))
        self.assertEqual(add_lists([], (1, 2, 3)), (1, 2, 3))
        self.assertEqual(add_lists((1, 2, 3), []), (1, 2, 3))

    def test_empty_inputs(self):
        self.assertEqual(add_lists([], []), [])

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            add_lists([1, 2, 3], 'abc')

    def test_list_with_tuple(self):
        self.assertEqual(add_lists([(1, 2, 3)], [4, 5, 6]), [(1, 2, 3), 4, 5, 6])

    def test_tuple_with_list(self):
        self.assertEqual(add_lists(((1, 2, 3)), [4, 5, 6]), (1, 2, 3, 4, 5, 6))
