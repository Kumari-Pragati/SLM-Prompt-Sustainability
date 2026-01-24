import unittest
from mbpp_37_code import sort_mixed_list

class TestSortMixedList(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(sort_mixed_list([3, 'a', 1, 'b']), [1, 3, 'a', 'b'])

    def test_empty_input(self):
        self.assertEqual(sort_mixed_list([]), [])

    def test_all_integers(self):
        self.assertEqual(sort_mixed_list([5, 3, 1]), [1, 3, 5])

    def test_all_strings(self):
        self.assertEqual(sort_mixed_list(['b', 'a', 'c']), ['a', 'b', 'c'])

    def test_mixed_integers_and_strings(self):
        self.assertEqual(sort_mixed_list([3, 'b', 1, 'a']), [1, 3, 'a', 'b'])

    def test_duplicate_elements(self):
        self.assertEqual(sort_mixed_list([3, 'a', 3, 'a']), [3, 3, 'a', 'a'])
