import unittest
from mbpp_709_code import defaultdict

class TestGetUnique(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(get_unique([(1, 'a'), (2, 'a'), (3, 'b'), (4, 'a'), (5, 'c'), (6, 'a')]), "'{'a': 3, 'b': 1, 'c': 1}'")

    def test_empty_list(self):
        self.assertEqual(get_unique([]), "'{}'")

    def test_single_element_list(self):
        self.assertEqual(get_unique([(1, 'a')]), "'{'a': 1}'")

    def test_duplicate_elements(self):
        self.assertEqual(get_unique([(1, 'a'), (1, 'a'), (2, 'b'), (2, 'b')]), "'{'a': 2, 'b': 2}'")

    def test_mixed_elements(self):
        self.assertEqual(get_unique([(1, 'a'), (2, 'b'), (3, 'a'), (4, 'c'), (5, 'a')]), "'{'a': 3, 'b': 1, 'c': 1}'")

    def test_negative_key(self):
        self.assertRaises(KeyError, get_unique, [(-1, 'a'), (0, 'b')])

    def test_non_hashable_key(self):
        self.assertRaises(TypeError, get_unique, [(1, [1, 2, 3]), (2, [4, 5, 6])])
