import unittest
from mbpp_561_code import assign_elements

class TestAssignElements(unittest.TestCase):

    def test_simple(self):
        self.assertDictEqual(assign_elements([(1, 1), (2, 2), (1, 2)]), {'1': [1, 2], '2': [2]})
        self.assertDictEqual(assign_elements([('a', 'a'), ('b', 'b'), ('a', 'b')]), {'a': ['a', 'b'], 'b': ['b']})

    def test_edge_cases(self):
        self.assertDictEqual(assign_elements([(1, 1), (2, 2)]), {'1': [1], '2': [2]})
        self.assertDictEqual(assign_elements([(1, 1), (1, 2)]), {'1': [1, 2], '2': []})
        self.assertDictEqual(assign_elements([('a', 'a'), ('b', 'c')]), {'a': ['a'], 'b': ['c']})
        self.assertDictEqual(assign_elements([('a', 'a'), ('a', 'b')]), {'a': ['a', 'b'], 'b': []})

    def test_complex(self):
        self.assertDictEqual(assign_elements([(1, 1), (2, 2), (1, 2), (2, 1)]), {'1': [1, 2], '2': [2, 1]})
        self.assertDictEqual(assign_elements([('a', 'a'), ('b', 'b'), ('a', 'b'), ('b', 'a')]), {'a': ['a', 'b'], 'b': ['b', 'a']})
