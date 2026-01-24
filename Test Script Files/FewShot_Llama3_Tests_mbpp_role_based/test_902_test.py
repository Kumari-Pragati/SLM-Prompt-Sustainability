import unittest
from mbpp_902_code import add_dict

class TestAddDict(unittest.TestCase):
    def test_add_dict_empty(self):
        self.assertEqual(add_dict({}, {}), Counter())

    def test_add_dict_single(self):
        self.assertEqual(add_dict({'a': 1}, {}), Counter({'a': 1}))

    def test_add_dict_multiple(self):
        self.assertEqual(add_dict({'a': 1, 'b': 2}, {'b': 3, 'c': 4}), Counter({'a': 1, 'b': 5, 'c': 4}))

    def test_add_dict_duplicates(self):
        self.assertEqual(add_dict({'a': 1, 'a': 2}, {'a': 3}), Counter({'a': 6}))

    def test_add_dict_negative(self):
        self.assertEqual(add_dict({'a': 1, 'b': -2}, {'b': 3}), Counter({'a': 1, 'b': 1}))

    def test_add_dict_non_integer(self):
        with self.assertRaises(TypeError):
            add_dict({'a': 1, 'b':'string'}, {})
