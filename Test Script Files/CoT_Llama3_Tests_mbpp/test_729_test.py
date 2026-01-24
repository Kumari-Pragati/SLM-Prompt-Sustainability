import unittest
from mbpp_729_code import add_list

class TestAddList(unittest.TestCase):

    def test_add_list_typical(self):
        self.assertEqual(add_list([1, 2, 3], [4, 5, 6]), [5, 7, 9])

    def test_add_list_empty_list(self):
        self.assertEqual(add_list([], [1, 2, 3]), [])
        self.assertEqual(add_list([1, 2, 3], []), [])

    def test_add_list_single_element(self):
        self.assertEqual(add_list([1], [2]), [3])
        self.assertEqual(add_list([1], []), [1])
        self.assertEqual(add_list([], [1]), [1])

    def test_add_list_negative_numbers(self):
        self.assertEqual(add_list([-1, 1], [1, -1]), [1, 0])

    def test_add_list_non_integer_values(self):
        with self.assertRaises(TypeError):
            add_list([1, 2, 'a'], [3, 4, 5])

    def test_add_list_mixed_types(self):
        with self.assertRaises(TypeError):
            add_list([1, 2, 3.0], [4, 5, 'a'])
