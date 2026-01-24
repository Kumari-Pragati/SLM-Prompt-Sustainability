import unittest
from mbpp_833_code import get_key

class TestGetKey(unittest.TestCase):

    def test_get_key(self):
        dict1 = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual(get_key(dict1), ['a', 'b', 'c'])

        dict2 = {'x': 4, 'y': 5, 'z': 6}
        self.assertEqual(get_key(dict2), ['x', 'y', 'z'])

        dict3 = {}
        self.assertEqual(get_key(dict3), [])

        dict4 = {'p': 7, 'q': 8, 'r': 9,'s': 10}
        self.assertEqual(get_key(dict4), ['p', 'q', 'r','s'])

    def test_get_key_empty_dict(self):
        dict_empty = {}
        self.assertEqual(get_key(dict_empty), [])

    def test_get_key_non_dict(self):
        with self.assertRaises(TypeError):
            get_key(123)
