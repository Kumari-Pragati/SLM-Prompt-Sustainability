import unittest
from mbpp_893_code import Extract

class TestExtract(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(Extract([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [3, 6, 9])

    def test_empty_list(self):
        self.assertEqual(Extract([]), [])

    def test_single_item_list(self):
        self.assertEqual(Extract([[1]]), [1])

    def test_negative_index(self):
        self.assertEqual(Extract([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]), [3, 6, 9])

    def test_list_of_strings(self):
        self.assertEqual(Extract([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]), ['c', 'f', 'i'])

    def test_list_of_tuples(self):
        self.assertEqual(Extract([(1, 2, 3), (4, 5, 6), (7, 8, 9)]), [3, 6, 9])
