import unittest
from mbpp_37_code import sort_mixed_list

class TestSortMixedList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sort_mixed_list([]), [])

    def test_int_list(self):
        self.assertEqual(sort_mixed_list([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_str_list(self):
        self.assertEqual(sort_mixed_list(['a', 'b', 'c', 'd', 'e']), ['a', 'b', 'c', 'd', 'e'])

    def test_mixed_list(self):
        self.assertEqual(sort_mixed_list([1, 'a', 2, 'b', 3, 'c', 4, 'd', 5, 'e']), [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e'])

    def test_mixed_list_with_duplicates(self):
        self.assertEqual(sort_mixed_list([1, 'a', 2, 2, 'b', 3, 'c', 4, 4, 'd', 5, 5, 'e']), [1, 2, 2, 3, 4, 4, 5, 5, 'a', 'b', 'c', 'd', 'e'])
