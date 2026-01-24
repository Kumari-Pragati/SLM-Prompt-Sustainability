import unittest
from mbpp_37_code import sort_mixed_list

class TestSortMixedList(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sort_mixed_list([]), [])

    def test_all_ints(self):
        self.assertEqual(sort_mixed_list([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_all_strings(self):
        self.assertEqual(sort_mixed_list(['a', 'b', 'c', 'd', 'e']), ['a', 'b', 'c', 'd', 'e'])

    def test_mixed_list(self):
        self.assertEqual(sort_mixed_list([1, 'a', 2, 'b', 3, 'c']), [1, 2, 3, 'a', 'b', 'c'])

    def test_empty_string(self):
        self.assertEqual(sort_mixed_list(['', 'a', 1, 'b', 2]), ['', 'a', 'b', 1, 2])

    def test_negative_numbers(self):
        self.assertEqual(sort_mixed_list([-1, -2, 1, 'a', 'b']), [-2, -1, 1, 'a', 'b'])

    def test_duplicates(self):
        self.assertEqual(sort_mixed_list([1, 2, 2, 3, 1, 'a', 'b', 'c']), [1, 1, 2, 2, 3, 'a', 'b', 'c'])
