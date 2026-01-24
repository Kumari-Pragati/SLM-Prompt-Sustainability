import unittest
from mbpp_37_code import sort_mixed_list

class TestSortMixedList(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sort_mixed_list([]), [])

    def test_single_type_list(self):
        self.assertEqual(sort_mixed_list([1, 2, 3]), [1, 2, 3])
        self.assertEqual(sort_mixed_list(['a', 'b', 'c']), ['a', 'b', 'c'])

    def test_mixed_list(self):
        self.assertEqual(sort_mixed_list([1, 'a', 2, 'b', 3, 'c']), [1, 2, 3, 'a', 'b', 'c'])

    def test_empty_list_with_type(self):
        self.assertEqual(sort_mixed_list([1, 'a']), [1, 'a'])

    def test_negative_numbers(self):
        self.assertEqual(sort_mixed_list([-1, -2, 3, 'a', 'b']), [-2, -1, 3, 'a', 'b'])

    def test_string_with_numbers(self):
        self.assertEqual(sort_mixed_list(['a', 1, 'b', 2, 'c', 3]), [1, 2, 3, 'a', 'b', 'c'])

    def test_string_with_numbers_and_empty(self):
        self.assertEqual(sort_mixed_list(['a', 1, 'b', 2, 'c', 3, 'd']), [1, 2, 3, 'a', 'b', 'c', 'd'])
