import unittest
from mbpp_37_code import sort_mixed_list

class TestSortMixedList(unittest.TestCase):
    def test_sort_mixed_list_with_ints_and_strings(self):
        self.assertEqual(sort_mixed_list([1, 2, 'a', 'b', 3]), [1, 1, 2, 2, 3, 'a', 'b'])

    def test_sort_mixed_list_with_only_ints(self):
        self.assertEqual(sort_mixed_list([1, 2, 3]), [1, 2, 3])

    def test_sort_mixed_list_with_only_strings(self):
        self.assertEqual(sort_mixed_list(['a', 'b', 'c']), ['a', 'b', 'c'])

    def test_sort_mixed_list_with_empty_list(self):
        self.assertEqual(sort_mixed_list([]), [])

    def test_sort_mixed_list_with_int_and_string_in_reverse_order(self):
        self.assertEqual(sort_mixed_list([3, 'b', 2, 'a', 1]), [1, 1, 2, 2, 3, 'a', 'b'])

    def test_sort_mixed_list_with_duplicate_ints(self):
        self.assertEqual(sort_mixed_list([1, 1, 2, 2, 3]), [1, 1, 2, 2, 3])

    def test_sort_mixed_list_with_duplicate_strings(self):
        self.assertEqual(sort_mixed_list(['a', 'a', 'b', 'b', 'c']), ['a', 'a', 'b', 'b', 'c'])

    def test_sort_mixed_list_with_int_and_float(self):
        self.assertEqual(sort_mixed_list([1.0, 2, 3.0]), [1.0, 2, 3.0])

    def test_sort_mixed_list_with_int_and_complex(self):
        self.assertEqual(sort_mixed_list([1j, 2, 3]), [1j, 2, 3])

    def test_sort_mixed_list_with_invalid_input(self):
        with self.assertRaises(TypeError):
            sort_mixed_list([1, 'a', True])
