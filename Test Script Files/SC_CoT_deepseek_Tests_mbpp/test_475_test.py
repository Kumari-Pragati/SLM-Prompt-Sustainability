import unittest
from mbpp_475_code import sort_counter

class TestSortCounter(unittest.TestCase):

    def test_typical_case(self):
        data = {'a': 1, 'b': 2, 'c': 3}
        result = sort_counter(data)
        self.assertEqual(result, [('c', 3), ('b', 2), ('a', 1)])

    def test_single_element(self):
        data = {'a': 1}
        result = sort_counter(data)
        self.assertEqual(result, [('a', 1)])

    def test_empty_dict(self):
        data = {}
        result = sort_counter(data)
        self.assertEqual(result, [])

    def test_negative_values(self):
        data = {'a': -1, 'b': -2, 'c': -3}
        result = sort_counter(data)
        self.assertEqual(result, [('c', -3), ('b', -2), ('a', -1)])

    def test_zero_values(self):
        data = {'a': 0, 'b': 0, 'c': 0}
        result = sort_counter(data)
        self.assertEqual(result, [('c', 0), ('b', 0), ('a', 0)])

    def test_large_numbers(self):
        data = {'a': 1000000, 'b': 2000000, 'c': 3000000}
        result = sort_counter(data)
        self.assertEqual(result, [('c', 3000000), ('b', 2000000), ('a', 1000000)])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sort_counter('not a dictionary')
