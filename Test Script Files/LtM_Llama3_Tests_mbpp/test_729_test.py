import unittest
from mbpp_729_code import add_list

class TestAddList(unittest.TestCase):
    def test_empty_lists(self):
        self.assertEqual(add_list([], []), [])

    def test_single_element_lists(self):
        self.assertEqual(add_list([1], [2]), [3])
        self.assertEqual(add_list([1], []), [1])
        self.assertEqual(add_list([], [1]), [1])

    def test_multiple_element_lists(self):
        self.assertEqual(add_list([1, 2, 3], [4, 5, 6]), [5, 7, 9])
        self.assertEqual(add_list([1, 2, 3], []), [1, 2, 3])
        self.assertEqual(add_list([], [1, 2, 3]), [1, 2, 3])

    def test_edge_cases(self):
        self.assertEqual(add_list([-1, 0, 1], [1, 0, -1]), [0, 0, 0])
        self.assertEqual(add_list([1, 2, 3], [-1, -2, -3]), [0, 0, 0])

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            add_list('a', [1, 2, 3])
        with self.assertRaises(TypeError):
            add_list([1, 2, 3], 'a')
