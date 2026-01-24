import unittest
from mbpp_333_code import Sort

class TestSort(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(Sort([]), [])

    def test_single_element_list(self):
        self.assertEqual(Sort([['a', 1]]), [['a', 1]])

    def test_multiple_elements_list(self):
        self.assertEqual(Sort([['c', 3], ['a', 1], ['b', 2]]), [['a', 1], ['b', 2], ['c', 3]])

    def test_list_with_duplicates(self):
        self.assertEqual(Sort([['c', 3], ['a', 1], ['b', 2], ['c', 3]]), [['a', 1], ['b', 2], ['c', 3], ['c', 3]])

    def test_list_with_negative_numbers(self):
        self.assertEqual(Sort([['c', -3], ['a', 1], ['b', 2]]), [['c', -3], ['a', 1], ['b', 2]])
