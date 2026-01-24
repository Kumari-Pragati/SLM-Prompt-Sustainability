import unittest
from mbpp_902_code import Counter
from mbpp_902_code import add_dict

class TestAddDict(unittest.TestCase):

    def test_add_dict(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'b': 3, 'c': 4}
        expected_result = Counter({'a': 1, 'b': 5, 'c': 4})
        self.assertEqual(add_dict(d1, d2), expected_result)

    def test_add_dict_empty_dict(self):
        d1 = {}
        d2 = {'b': 3, 'c': 4}
        expected_result = Counter({'b': 3, 'c': 4})
        self.assertEqual(add_dict(d1, d2), expected_result)

    def test_add_dict_same_keys(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'a': 3, 'b': 4}
        expected_result = Counter({'a': 4, 'b': 6})
        self.assertEqual(add_dict(d1, d2), expected_result)

    def test_add_dict_different_keys(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'c': 3, 'd': 4}
        expected_result = Counter({'a': 1, 'b': 2, 'c': 3, 'd': 4})
        self.assertEqual(add_dict(d1, d2), expected_result)
