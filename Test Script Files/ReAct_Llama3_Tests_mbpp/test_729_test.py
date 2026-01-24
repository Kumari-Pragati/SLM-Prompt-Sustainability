import unittest
from mbpp_729_code import add_list

class TestAddList(unittest.TestCase):
    def test_empty_lists(self):
        self.assertEqual(add_list([], []), [])

    def test_single_element_lists(self):
        self.assertEqual(add_list([1], [2]), [3])
        self.assertEqual(add_list([1, 2, 3], []), [1, 2, 3])
        self.assertEqual(add_list([], [1, 2, 3]), [1, 2, 3])

    def test_multiple_element_lists(self):
        self.assertEqual(add_list([1, 2, 3], [4, 5, 6]), [5, 7, 9])
        self.assertEqual(add_list([-1, 2, 3], [4, -5, 6]), [3, 7, 9])
        self.assertEqual(add_list([1, 2, 3], [-4, 5, -6]), [3, 7, 9])

    def test_lists_of_different_lengths(self):
        self.assertEqual(add_list([1, 2, 3], [4, 5]), [5, 7])
        self.assertEqual(add_list([1, 2, 3, 4, 5], [4, 5, 6]), [5, 7, 9, 10, 11])

    def test_lists_with_zero(self):
        self.assertEqual(add_list([1, 2, 3], [0, 0, 0]), [1, 2, 3])
        self.assertEqual(add_list([0, 0, 0], [1, 2, 3]), [1, 2, 3])
