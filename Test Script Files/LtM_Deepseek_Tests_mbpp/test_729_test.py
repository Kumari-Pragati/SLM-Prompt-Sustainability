import unittest
from mbpp_729_code import add_list

class TestAddList(unittest.TestCase):
    def test_simple_addition(self):
        self.assertEqual(add_list([1, 2, 3], [4, 5, 6]), [5, 7, 9])

    def test_empty_lists(self):
        self.assertEqual(add_list([], []), [])

    def test_different_lengths(self):
        self.assertEqual(add_list([1, 2, 3], [4, 5]), [5, 7, 3])

    def test_negative_numbers(self):
        self.assertEqual(add_list([-1, 2, -3], [4, -5, 6]), [3, -3, 3])

    def test_large_numbers(self):
        self.assertEqual(add_list([1000000, 2000000], [3000000, 4000000]), [4000000, 6000000])
