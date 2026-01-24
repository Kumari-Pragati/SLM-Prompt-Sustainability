import unittest
from mbpp_902_code import add_dict

class TestAddDict(unittest.TestCase):

    def test_add_dict(self):
        d1 = {'a': 1, 'b': 2, 'c': 3}
        d2 = {'c': 4, 'd': 5, 'e': 6}
        result = add_dict(d1, d2)
        self.assertEqual(result, Counter({'a': 1, 'b': 2, 'c': 7, 'd': 5, 'e': 6}))

    def test_add_dict_empty(self):
        d1 = {}
        d2 = {}
        result = add_dict(d1, d2)
        self.assertEqual(result, Counter())

    def test_add_dict_one_empty(self):
        d1 = {'a': 1, 'b': 2, 'c': 3}
        d2 = {}
        result = add_dict(d1, d2)
        self.assertEqual(result, Counter({'a': 1, 'b': 2, 'c': 3}))

    def test_add_dict_one_non_empty(self):
        d1 = {}
        d2 = {'c': 4, 'd': 5, 'e': 6}
        result = add_dict(d1, d2)
        self.assertEqual(result, Counter({'c': 4, 'd': 5, 'e': 6}))

    def test_add_dict_non_empty(self):
        d1 = {'a': 1, 'b': 2, 'c': 3}
        d2 = {'c': 4, 'd': 5, 'e': 6}
        result = add_dict(d1, d2)
        self.assertEqual(result, Counter({'a': 1, 'b': 2, 'c': 7, 'd': 5, 'e': 6}))
