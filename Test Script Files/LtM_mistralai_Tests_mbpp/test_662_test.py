import unittest
from mbpp_662_code import sorted_dict

class TestSortedDict(unittest.TestCase):

    def test_simple(self):
        self.assertDictEqual(sorted_dict({'a': [1, 3, 5], 'b': [2, 4, 6]}), {'a': [1, 3, 5], 'b': [2, 4, 6]})
        self.assertDictEqual(sorted_dict({'x': [9, 7, 5], 'y': [1, 3, 8]}), {'x': [5, 7, 9], 'y': [1, 3, 8]})

    def test_edge_cases(self):
        self.assertDictEqual(sorted_dict({'a': [1], 'b': []}), {'a': [1], 'b': []})
        self.assertDictEqual(sorted_dict({'a': [], 'b': [1]}), {'a': [], 'b': [1]})
        self.assertDictEqual(sorted_dict({'a': [1, 1], 'b': [2, 2]}), {'a': [1, 1], 'b': [2, 2]})

    def test_complex(self):
        self.assertDictEqual(sorted_dict({'a': [1, 3, 5, 1], 'b': [2, 4, 6, 2]}), {'a': [1, 1, 3, 5], 'b': [2, 2, 4, 6]})
        self.assertDictEqual(sorted_dict({'a': [1, 3, 5, 1], 'b': [2, 4, 6, 2, 2]}), {'a': [1, 1, 3, 5], 'b': [2, 2, 4, 6, 2]})
        self.assertDictEqual(sorted_dict({'a': [1, 3, 5, 1], 'b': [2, 4, 6, 2, 2, 2]}), {'a': [1, 1, 3, 5], 'b': [2, 2, 4, 6, 2, 2]})
