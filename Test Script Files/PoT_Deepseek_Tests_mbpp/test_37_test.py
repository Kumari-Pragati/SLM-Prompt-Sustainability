import unittest
from mbpp_37_code import sort_mixed_list

class TestSortMixedList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sort_mixed_list([3, 'a', 1, 'b', 2]), [1, 2, 3, 'a', 'b'])

    def test_empty_list(self):
        self.assertEqual(sort_mixed_list([]), [])

    def test_all_integers(self):
        self.assertEqual(sort_mixed_list([3, 1, 2]), [1, 2, 3])

    def test_all_strings(self):
        self.assertEqual(sort_mixed_list(['b', 'a', 'c']), ['a', 'b', 'c'])

    def test_mixed_integers_and_strings(self):
        self.assertEqual(sort_mixed_list([3, 'b', 1, 'a', 2]), [1, 2, 3, 'a', 'b'])

    def test_duplicate_values(self):
        self.assertEqual(sort_mixed_list([3, 'a', 3, 'b', 1, 'a', 2]), [1, 2, 3, 'a', 'a', 'b'])

    def test_large_integers(self):
        self.assertEqual(sort_mixed_list([1000000000, 'a', 1, 'b', 2]), [1, 2, 1000000000, 'a', 'b'])

    def test_negative_integers(self):
        self.assertEqual(sort_mixed_list([-3, 'a', -1, 'b', -2]), [-3, -2, -1, 'a', 'b'])
