import unittest
from mbpp_333_code import Sort

class TestSortFunction(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(Sort([]), [])

    def test_single_element_list(self):
        self.assertEqual(Sort([['a', 1]]), [['a', 1]])

    def test_multiple_elements_list(self):
        self.assertEqual(Sort([['b', 3], ['a', 1], ['c', 2]]), [['a', 1], ['c', 2], ['b', 3]])

    def test_list_with_duplicates(self):
        self.assertEqual(Sort([['b', 3], ['a', 1], ['c', 2], ['b', 3]]), [['a', 1], ['b', 3], ['b', 3], ['c', 2]])

    def test_list_with_negative_numbers(self):
        self.assertEqual(Sort([['b', -3], ['a', 1], ['c', 2]]), [['a', 1], ['c', 2], ['b', -3]])

    def test_list_with_non_integer_values(self):
        self.assertEqual(Sort([['b', 3.5], ['a', 1.2], ['c', 2.7]]), [['a', 1.2], ['c', 2.7], ['b', 3.5]])
