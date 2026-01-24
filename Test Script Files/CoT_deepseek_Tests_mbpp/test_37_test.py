import unittest
from mbpp_37_code import sort_mixed_list

class TestSortMixedList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sort_mixed_list([3, 'a', 1, 'b', 2]), [1, 2, 3, 'a', 'b'])

    def test_empty_list(self):
        self.assertEqual(sort_mixed_list([]), [])

    def test_all_integers(self):
        self.assertEqual(sort_mixed_list([5, 3, 1, 4, 2]), [1, 2, 3, 4, 5])

    def test_all_strings(self):
        self.assertEqual(sort_mixed_list(['c', 'a', 'b', 'd']), ['a', 'b', 'c', 'd'])

    def test_mixed_integers_and_strings(self):
        self.assertEqual(sort_mixed_list([3, 'b', 1, 'a', 2]), [1, 2, 3, 'a', 'b'])

    def test_duplicates(self):
        self.assertEqual(sort_mixed_list([3, 'a', 1, 'a', 2, 2]), [1, 2, 2, 3, 'a', 'a'])

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            sort_mixed_list([3, 'a', 1, None, 2])
