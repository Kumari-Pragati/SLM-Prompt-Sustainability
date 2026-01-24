import unittest
from mbpp_662_code import sorted_dict

class TestSortedDict(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(sorted_dict({'a': [3, 2, 1]}), {'a': [1, 2, 3]})

    def test_edge_conditions(self):
        self.assertEqual(sorted_dict({}), {})
        self.assertEqual(sorted_dict({'a': []}), {'a': []})

    def test_complex_cases(self):
        self.assertEqual(sorted_dict({'a': [3, 2, 1], 'b': [5, 4, 3]}), {'a': [1, 2, 3], 'b': [3, 4, 5]})
        self.assertEqual(sorted_dict({'a': [3, 2, 1], 'b': []}), {'a': [1, 2, 3], 'b': []})
