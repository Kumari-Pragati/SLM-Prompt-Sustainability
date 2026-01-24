import unittest
from mbpp_465_code import drop_empty

class TestDropEmpty(unittest.TestCase):

    def test_simple_input(self):
        self.assertDictEqual(drop_empty({'a': 1, 'b': None, 'c': 3}), {'a': 1, 'c': 3})
        self.assertDictEqual(drop_empty({'a': 'str', 'b': None, 'c': 3.0}), {'a': 'str', 'c': 3.0})

    def test_edge_cases(self):
        self.assertDictEqual(drop_empty({None: 'x'}), {})
        self.assertDictEqual(drop_empty({'a': '', 'b': None, 'c': ' '}), {'a': '', 'c': ' '})
        self.assertDictEqual(drop_empty({'a': 0, 'b': None, 'c': -1}), {'a': 0, 'c': -1})

    def test_complex_input(self):
        self.assertDictEqual(drop_empty({'a': [1, None, 3], 'b': [None, 2, None], 'c': [4, 5, None]}),
                              {'a': [1, 3], 'c': [4, 5]})
        self.assertDictEqual(drop_empty({'a': {'key1': None, 'key2': 'val2'}, 'b': {'key3': None}, 'c': {'key4': 'val4'}}),
                              {'a': {'key2': 'val2'}, 'c': {'key4': 'val4'}})
