import unittest
from mbpp_37_code import sort_mixed_list

class TestSortMixedList(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sort_mixed_list([1, 3, 2, 'a', 'c', 'b']), [1, 2, 3, 'a', 'b', 'c'])

    def test_empty_list(self):
        self.assertEqual(sort_mixed_list([]), [])

    def test_list_with_single_element(self):
        self.assertEqual(sort_mixed_list([1]), [1])
        self.assertEqual(sort_mixed_list(['a']), ['a'])

    def test_list_with_integers_and_strings(self):
        self.assertEqual(sort_mixed_list([1, 'a', 2, 'b', 3, 'c']), [1, 2, 3, 'a', 'b', 'c'])

    def test_list_with_duplicates(self):
        self.assertEqual(sort_mixed_list([1, 2, 2, 'a', 'b', 'a']), [1, 2, 2, 'a', 'a', 'b'])

    def test_list_with_negative_numbers(self):
        self.assertEqual(sort_mixed_list([-1, 1, -2, 'a', 'b', 'c']), [-2, -1, 1, 'a', 'b', 'c'])
