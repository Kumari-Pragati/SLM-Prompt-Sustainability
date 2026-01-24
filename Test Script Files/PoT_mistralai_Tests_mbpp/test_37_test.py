import unittest
from mbpp_37_code import sort_mixed_list

class TestSortMixedList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sort_mixed_list([1, 'a', 3, 'b', 2]), [1, 2, 3, 'a', 'b'])

    def test_empty_list(self):
        self.assertEqual(sort_mixed_list([]), [])

    def test_single_int(self):
        self.assertEqual(sort_mixed_list([4]), [4])

    def test_single_string(self):
        self.assertEqual(sort_mixed_list(['z']), ['z'])

    def test_mixed_list_with_duplicates(self):
        self.assertEqual(sort_mixed_list([1, 'a', 1, 'b', 2, 'a']), [1, 1, 2, 'a', 'a', 'b'])

    def test_mixed_list_with_empty_strings(self):
        self.assertEqual(sort_mixed_list(['', 1, 'a', '', 2, 'b']), ['', 1, 2, 'a', 'b'])

    def test_mixed_list_with_long_strings(self):
        self.assertEqual(sort_mixed_list(['abc', 'xyz', 1, 'def', 2, 'ghi']), ['abc', 'def', 'ghi', 'xyz', 1, 2])

    def test_mixed_list_with_negative_numbers(self):
        self.assertEqual(sort_mixed_list([-1, 'a', 0, 'b', 1, 'c']), [-1, 0, 1, 'a', 'b', 'c'])

    def test_mixed_list_with_floats(self):
        self.assertEqual(sort_mixed_list([1.5, 'a', 2.0, 'b', 3.1, 'c']), [1.5, 2.0, 3.1, 'a', 'b', 'c'])
