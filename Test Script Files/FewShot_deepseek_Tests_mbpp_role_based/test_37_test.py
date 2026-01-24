import unittest
from mbpp_37_code import sort_mixed_list

class TestSortMixedList(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(sort_mixed_list([3, 'a', 1, 'b', 2]), [1, 2, 3, 'a', 'b'])

    def test_empty_list(self):
        self.assertEqual(sort_mixed_list([]), [])

    def test_list_with_only_strings(self):
        self.assertEqual(sort_mixed_list(['b', 'a']), ['a', 'b'])

    def test_list_with_only_integers(self):
        self.assertEqual(sort_mixed_list([3, 1, 2]), [1, 2, 3])

    def test_list_with_duplicates(self):
        self.assertEqual(sort_mixed_list([3, 'a', 1, 'a', 2]), [1, 2, 3, 'a', 'a'])

    def test_list_with_mixed_duplicates(self):
        self.assertEqual(sort_mixed_list([3, 'a', 1, 'b', 2, 'a', 'b']), [1, 2, 3, 'a', 'a', 'b', 'b'])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sort_mixed_list(123)
