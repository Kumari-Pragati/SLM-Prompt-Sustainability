import unittest
from mbpp_37_code import sort_mixed_list

class TestSortMixedList(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sort_mixed_list([]), [])

    def test_integers_only(self):
        self.assertEqual(sort_mixed_list([1, 3, 2, 4]), [1, 2, 3, 4])

    def test_strings_only(self):
        self.assertEqual(sort_mixed_list(['a', 'c', 'b']), ['a', 'b', 'c'])

    def test_mixed_list(self):
        self.assertEqual(sort_mixed_list([1, 'a', 3, 'c', 2, 'b', 4]), [1, 2, 3, 4, 'a', 'b', 'c'])

    def test_list_with_duplicates(self):
        self.assertEqual(sort_mixed_list([1, 1, 'a', 'a', 2, 3, 3, 'b', 'c']), [1, 1, 2, 3, 3, 'a', 'a', 'b', 'c'])
