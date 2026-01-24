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
        self.assertEqual(sort_mixed_list([1, 'a', 3, 'c', 2, 'b']), [1, 2, 3, 'a', 'b', 'c'])

    def test_empty_list_with_duplicates(self):
        self.assertEqual(sort_mixed_list([1, 1, 2, 2, 3, 3]), [1, 1, 2, 2, 3, 3])

    def test_empty_list_with_negative_numbers(self):
        self.assertEqual(sort_mixed_list([-1, -2, -3]), [-3, -2, -1])

    def test_empty_list_with_empty_strings(self):
        self.assertEqual(sort_mixed_list(['', '', 'a']), ['', '', 'a'])
