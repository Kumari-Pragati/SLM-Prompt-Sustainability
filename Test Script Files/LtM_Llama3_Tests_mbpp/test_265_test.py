import unittest
from mbpp_265_code import list_split

class TestListSplit(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(list_split('abc', 1), ['a', 'b', 'c'])
        self.assertEqual(list_split('abc', 2), ['ab', 'c'])
        self.assertEqual(list_split('abc', 3), ['abc'])

    def test_edge(self):
        self.assertEqual(list_split('', 1), [])
        self.assertEqual(list_split('a', 0), [])
        self.assertEqual(list_split('a', 1), ['a'])

    def test_invalid(self):
        with self.assertRaises(TypeError):
            list_split(None, 1)
        with self.assertRaises(TypeError):
            list_split('a', None)
