import unittest
from mbpp_37_code import sort_mixed_list

class TestSortMixedList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sort_mixed_list([]), [])

    def test_all_ints(self):
        self.assertEqual(sort_mixed_list([1, 3, 5, 7, 9]), [1, 3, 5, 7, 9])

    def test_all_strings(self):
        self.assertEqual(sort_mixed_list(['a', 'b', 'c', 'd', 'e']), ['a', 'b', 'c', 'd', 'e'])

    def test_mixed_int_strings(self):
        self.assertEqual(sort_mixed_list([1, 'a', 3, 'b', 5, 'c', 7, 'd', 9, 'e']), [1, 'a', 3, 'b', 5, 'c', 7, 'd', 9, 'e'])

    def test_mixed_order(self):
        self.assertEqual(sort_mixed_list(['e', 9, 'd', 7, 'c', 5, 'b', 3, 'a', 1]), ['a', 1, 'b', 3, 'c', 5, 'd', 7, 'e', 9])

    def test_int_and_float(self):
        self.assertEqual(sort_mixed_list([1.0, 2.0, 3, 4.0, 5]), [1.0, 2.0, 3, 4.0, 5])

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            sort_mixed_list([1, 'a', 3, [4, 5], 'b'])
