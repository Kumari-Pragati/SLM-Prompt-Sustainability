import unittest
from mbpp_902_code import Counter
from copy import deepcopy

def add_dict(d1, d2):
    add_dict = Counter(d1) + Counter(d2)
    return add_dict

class TestAddDict(unittest.TestCase):

    def test_empty_dicts(self):
        self.assertDictEqual(add_dict({}, {}), Counter())

    def test_single_element_dicts(self):
        self.assertDictEqual(add_dict({'a': 1}, {}), {'a': 1})
        self.assertDictEqual(add_dict({}, {'a': 1}), {'a': 1})

    def test_equal_dicts(self):
        d1 = {'a': 1, 'b': 2}
        d2 = deepcopy(d1)
        self.assertDictEqual(add_dict(d1, d2), Counter({'a': 2, 'b': 2}))

    def test_different_dicts(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'c': 3, 'd': 4}
        self.assertDictEqual(add_dict(d1, d2), {'a': 1, 'b': 2, 'c': 3, 'd': 4})
