import unittest
from mbpp_475_code import sort_counter

class TestSortCounter(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sort_counter({'a': 2, 'b': 1, 'c': 3}), [('c', 3), ('a', 2), ('b', 1)])

    def test_edge_case_single_key(self):
        self.assertEqual(sort_counter({'a': 1}), [('a', 1)])

    def test_edge_case_multiple_keys(self):
        self.assertEqual(sort_counter({'a': 100, 'b': 100, 'c': 1}), [('c', 1), ('a', 100), ('b', 100)])

    def test_corner_case_empty_dict(self):
        self.assertEqual(sort_counter({}), [])

    def test_invalid_input_non_dict(self):
        self.assertRaises(TypeError, sort_counter, 123)
