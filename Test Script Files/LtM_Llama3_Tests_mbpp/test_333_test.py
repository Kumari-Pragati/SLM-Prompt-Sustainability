import unittest
from mbpp_333_code import Sort

class TestSortFunction(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(Sort([]), [])

    def test_single_element_list(self):
        self.assertEqual(Sort([['a', 1]]), [['a', 1]])

    def test_multiple_elements_list(self):
        self.assertEqual(Sort([['a', 1], ['b', 2], ['c', 3]]), [['c', 3], ['b', 2], ['a', 1]])

    def test_empty_list_with_duplicates(self):
        self.assertEqual(Sort([['a', 1], ['a', 2], ['a', 3]]), [['a', 1], ['a', 2], ['a', 3]])

    def test_list_with_duplicates(self):
        self.assertEqual(Sort([['a', 1], ['b', 2], ['c', 3], ['a', 4], ['b', 5]]), [['c', 3], ['b', 5], ['a', 4], ['a', 1], ['b', 2]])

    def test_list_with_empty_sublist(self):
        self.assertEqual(Sort([['a', 1], ['b', 2], ['', 3], ['c', 4]]), [['c', 4], ['b', 2], ['', 3], ['a', 1]])

    def test_list_with_negative_values(self):
        self.assertEqual(Sort([['a', -1], ['b', 2], ['c', 3], ['d', -2]]), [['d', -2], ['a', -1], ['b', 2], ['c', 3]])
