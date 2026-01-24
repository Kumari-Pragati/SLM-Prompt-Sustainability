import unittest
from mbpp_902_code import Counter
from ninety_two_code import add_dict

class TestAddDict(unittest.TestCase):

    def test_empty_dicts(self):
        self.assertDictEqual(add_dict({}, {}), Counter())

    def test_single_dict(self):
        self.assertDictEqual(add_dict({'a': 1, 'b': 2}, {}), Counter({'a': 1, 'b': 2}))
        self.assertDictEqual(add_dict({}, {'a': 1, 'b': 2}), Counter({'a': 1, 'b': 2}))

    def test_equal_dicts(self):
        self.assertDictEqual(add_dict({'a': 1, 'b': 2}, {'a': 1, 'b': 2}), Counter({'a': 2, 'b': 2}))

    def test_different_keys(self):
        self.assertDictEqual(add_dict({'a': 1, 'b': 2}, {'c': 3, 'd': 4}), Counter({'a': 1, 'b': 2, 'c': 3, 'd': 4}))

    def test_same_key_different_values(self):
        self.assertDictEqual(add_dict({'a': 1, 'b': 2}, {'a': 3, 'b': 4}), Counter({'a': 4, 'b': 6}))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            add_dict(1, 2)
        with self.assertRaises(TypeError):
            add_dict({}, 1)
        with self.assertRaises(TypeError):
            add_dict(1, {})
