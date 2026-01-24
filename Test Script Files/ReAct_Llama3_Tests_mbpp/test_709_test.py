import unittest
from mbpp_709_code import get_unique

class TestGetUnique(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(get_unique([]), '{}')

    def test_single_element(self):
        self.assertEqual(get_unique([['a', 'b']]), {'b': 1})

    def test_multiple_elements(self):
        self.assertEqual(get_unique([['a', 'b'], ['b', 'c'], ['c', 'd']]), {'b': 2, 'c': 2, 'd': 1})

    def test_duplicates(self):
        self.assertEqual(get_unique([['a', 'b'], ['b', 'c'], ['c', 'b']]), {'b': 2, 'c': 2})

    def test_empty_sublists(self):
        self.assertEqual(get_unique([[], ['a', 'b'], ['b', 'c']]), {'b': 2, 'c': 1})

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            get_unique('test')

    def test_non_list_sublists(self):
        with self.assertRaises(TypeError):
            get_unique([['a', 'b'], 'c', 'd'])
