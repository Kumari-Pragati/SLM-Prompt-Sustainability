import unittest
from mbpp_37_code import sort_mixed_list

class TestSortMixedList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sort_mixed_list([]), [])

    def test_all_ints(self):
        self.assertEqual(sort_mixed_list([1, 3, 5, 7, 9]), [1, 3, 5, 7, 9])

    def test_all_strings(self):
        self.assertEqual(sort_mixed_list(['a', 'b', 'c', 'd', 'e']), ['a', 'b', 'c', 'd', 'e'])

    def test_mixed_ints_strings(self):
        self.assertEqual(sort_mixed_list([1, 'a', 3, 'b', 5, 'c', 7, 'd', 9, 'e']),
                         [1, 'a', 3, 'b', 5, 'c', 7, 'd', 9, 'e'])

    def test_int_edge_cases(self):
        self.assertEqual(sort_mixed_list([-10, -5, -1, 0, 1, 5, 10]), [-10, -5, -1, 0, 1, 5, 10])
        self.assertEqual(sort_mixed_list([-10, -5, -1, 0, 1, 5, 10, 100]), [-10, -5, -1, 0, 1, 5, 10, 100])

    def test_string_edge_cases(self):
        self.assertEqual(sort_mixed_list(['z', 'a', 'x', 'b', 'y', 'c', 'w', 'd', 'v', 'e']),
                         ['a', 'b', 'c', 'd', 'e', 'v', 'w', 'x', 'y', 'z'])
        self.assertEqual(sort_mixed_list(['z', 'a', 'x', 'b', 'y', 'c', 'w', 'd', 'v', 'e', 'Z']),
                         ['a', 'b', 'c', 'd', 'e', 'v', 'w', 'x', 'y', 'Z', 'z'])

    def test_mixed_int_string_edge_cases(self):
        self.assertEqual(sort_mixed_list([-10, 'z', -5, 'a', -1, 0, 'b', 1, 5, 'c', 10, 'd', 100, 'e']),
                         [-10, 'a', -5, 'b', -1, 0, 'c', 1, 5, 'd', 10, 'e', 100, 'z'])

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            sort_mixed_list([1, 'a', [1, 2, 3]])
