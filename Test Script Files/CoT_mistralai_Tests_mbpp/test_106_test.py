import unittest
from mbpp_106_code import add_lists

class TestAddLists(unittest.TestCase):
    def test_add_lists_with_empty_list(self):
        self.assertEqual(add_lists([], (1, 2, 3)), (1, 2, 3))

    def test_add_lists_with_empty_tuple(self):
        self.assertEqual(add_lists((1,), []), (1,))

    def test_add_lists_with_lists_and_tuples(self):
        self.assertEqual(add_lists([1, 2, 3], (4, 5, 6)), (1, 2, 3, 4, 5, 6))

    def test_add_lists_with_lists_and_single_element_tuple(self):
        self.assertEqual(add_lists([1, 2], (3,)), (1, 2, 3))

    def test_add_lists_with_lists_and_multiple_element_tuple(self):
        self.assertEqual(add_lists([1, 2], (3, 4, 5)), (1, 2, 3, 4, 5))

    def test_add_lists_with_lists_and_mixed_types(self):
        self.assertEqual(add_lists([1, 'a', 3.14], (2, 'b', 4)), (1, 'a', 3.14, 2, 'b', 4))

    def test_add_lists_with_tuples_and_lists_of_different_lengths(self):
        self.assertEqual(add_lists((1, 2, 3), [4, 5]), (1, 2, 3, 4, 5))

    def test_add_lists_with_invalid_input_list(self):
        with self.assertRaises(TypeError):
            add_lists('test', (1, 2, 3))

    def test_add_lists_with_invalid_input_tuple(self):
        with self.assertRaises(TypeError):
            add_lists([1, 2, 3], 'test')
