import unittest
from mbpp_729_code import add_list

class TestAddList(unittest.TestCase):
    def test_add_two_lists_of_same_length(self):
        self.assertEqual(add_list([1, 2, 3], [4, 5, 6]), [5, 7, 9])

    def test_add_two_lists_of_different_lengths_with_longer_list(self):
        self.assertEqual(add_list([1, 2, 3], [4, 5]), [5, 7, 3])

    def test_add_two_lists_of_different_lengths_with_shorter_list(self):
        self.assertEqual(add_list([1, 2], [4, 5, 6]), [5, 7])

    def test_empty_list(self):
        self.assertEqual(add_list([], []), [])

    def test_list_with_zero(self):
        self.assertEqual(add_list([0], [0]), [0])

    def test_list_with_negative_numbers(self):
        self.assertEqual(add_list([-1, -2, -3], [-4, -5, -6]), [-5, -7, -9])
