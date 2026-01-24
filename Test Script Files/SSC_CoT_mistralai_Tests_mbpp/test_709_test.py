import unittest
from mbpp_709_code import defaultdict
from 709_code import get_unique

class TestGetUnique(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(get_unique([('a', 1), ('b', 2), ('a', 1)]), "'{'a': 1, 'b': 1}'")
        self.assertEqual(get_unique([('x', 1), ('y', 2), ('z', 3), ('x', 1)]), "'{'x': 1, 'y': 1, 'z': 1}'")

    def test_edge_input(self):
        self.assertEqual(get_unique([('a', 1), ('a', 1)]), "'{'a': 2}'")
        self.assertEqual(get_unique([('a', 1), ('b', 2), ('a', 1), ('b', 2)]), "'{'a': 2, 'b': 2}'")
        self.assertEqual(get_unique([('a', 1), ('b', 2), ('a', 1), ('b', 2), ('a', 1)]), "'{'a': 3, 'b': 2}'")

    def test_empty_input(self):
        self.assertEqual(get_unique([]), "'{}'")

    def test_single_input(self):
        self.assertEqual(get_unique([('a', 1)]), "'{'a': 1}'")

    def test_invalid_input(self):
        self.assertRaises(TypeError, get_unique, [(1, 1)])
        self.assertRaises(TypeError, get_unique, [('a', 1.5)])
