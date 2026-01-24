import unittest
from mbpp_37_code import sort_mixed_list

class TestSortMixedList(unittest.TestCase):

    def test_typical_inputs(self):
        mixed_list = [1, 2, 3, 'a', 'b', 'c']
        self.assertEqual(sort_mixed_list(mixed_list), [1, 2, 3, 'a', 'b', 'c'])

    def test_edge_cases(self):
        mixed_list = [1, 2, 'a', 'b']
        self.assertEqual(sort_mixed_list(mixed_list), [1, 2, 'a', 'b'])
        mixed_list = [3, 2, 1, 'c', 'b', 'a']
        self.assertEqual(sort_mixed_list(mixed_list), [1, 2, 3, 'a', 'b', 'c'])
        mixed_list = ['c', 'b', 'a']
        self.assertEqual(sort_mixed_list(mixed_list), ['a', 'b', 'c'])

    def test_empty_list(self):
        mixed_list = []
        self.assertEqual(sort_mixed_list(mixed_list), [])

    def test_single_element_list(self):
        mixed_list = [1]
        self.assertEqual(sort_mixed_list(mixed_list), [1])
        mixed_list = ['a']
        self.assertEqual(sort_mixed_list(mixed_list), ['a'])

    def test_invalid_inputs(self):
        mixed_list = [1, 2, 3, 'a', 'b', 'c', 4.5]
        self.assertEqual(sort_mixed_list(mixed_list), [1, 2, 3, 'a', 'b', 'c'])
        mixed_list = [1, 2, 3, 'a', 'b', 'c', None]
        self.assertEqual(sort_mixed_list(mixed_list), [1, 2, 3, 'a', 'b', 'c'])
