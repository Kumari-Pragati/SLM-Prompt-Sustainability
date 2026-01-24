import unittest
from mbpp_37_code import sort_mixed_list

class TestSortMixedList(unittest.TestCase):

    def test_simple_list(self):
        self.assertEqual(sort_mixed_list([1, 'a', 2, 'b', 3]), [1, 1, 2, 2, 3, 'a', 'b'])

    def test_empty_list(self):
        self.assertEqual(sort_mixed_list([]), [])

    def test_single_int_list(self):
        self.assertEqual(sort_mixed_list([1]), [1])

    def test_single_str_list(self):
        self.assertEqual(sort_mixed_list(['a']), ['a'])

    def test_all_int_list(self):
        self.assertEqual(sort_mixed_list([1, 2, 3]), [1, 2, 3])

    def test_all_str_list(self):
        self.assertEqual(sort_mixed_list(['a', 'b', 'c']), ['a', 'b', 'c'])

    def test_mixed_list_with_duplicates(self):
        self.assertEqual(sort_mixed_list([1, 'a', 1, 'b', 2, 'a']), [1, 1, 1, 2, 'a', 'a', 'b'])

    def test_mixed_list_with_min_values(self):
        self.assertEqual(sort_mixed_list([-1, 'z', 0, 'a', -2]), [-2, -1, 0, 'a', 'z'])

    def test_mixed_list_with_max_values(self):
        self.assertEqual(sort_mixed_list([9, 'z', 10, 'a', 8]), [8, 9, 'a', 'z'])
