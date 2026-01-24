import unittest
from mbpp_69_code import is_sublist

class TestIsSublist(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(is_sublist([1, 2, 3, 4, 5], [2, 3]))
        self.assertTrue(is_sublist(['a', 'b', 'c', 'd'], ['a', 'b']))
        self.assertFalse(is_sublist([1, 2, 3, 4, 5], [6, 7]))
        self.assertFalse(is_sublist(['a', 'b', 'c', 'd'], ['e', 'f']))

    def test_empty_sublist(self):
        self.assertTrue(is_sublist([], []))
        self.assertTrue(is_sublist([1, 2, 3, 4, 5], []))
        self.assertTrue(is_sublist(['a', 'b', 'c', 'd'], []))

    def test_same_list(self):
        self.assertTrue(is_sublist([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))
        self.assertTrue(is_sublist(['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd']))

    def test_longer_sublist(self):
        self.assertFalse(is_sublist([1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6]))
        self.assertFalse(is_sublist(['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd', 'e']))

    def test_edge_cases(self):
        self.assertFalse(is_sublist([1, 2, 3, 4, 5], [6]))
        self.assertFalse(is_sublist(['a', 'b', 'c', 'd'], ['e']))
