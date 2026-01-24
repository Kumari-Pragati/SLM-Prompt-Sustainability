import unittest
from mbpp_561_code import assign_elements

class TestAssignElements(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(assign_elements([]), {})

    def test_single_element(self):
        self.assertEqual(assign_elements([('a', 'b')]), {'a': ['b'], 'b': ['b']})

    def test_multiple_elements(self):
        self.assertEqual(assign_elements([('a', 'b'), ('b', 'c'), ('c', 'a')]),
                         {'a': ['b', 'c'], 'b': ['c', 'b'], 'c': ['a', 'b']})

    def test_duplicates(self):
        self.assertEqual(assign_elements([('a', 'b'), ('b', 'b'), ('c', 'a')]),
                         {'a': ['b', 'c'], 'b': ['b', 'b'], 'c': ['a', 'b']})

    def test_empty_key(self):
        self.assertEqual(assign_elements([('None', 'b'), ('b', 'c')]),
                         {'None': ['b', 'c'], 'b': ['c', 'b']})

    def test_empty_value(self):
        self.assertEqual(assign_elements([('a', None), ('b', 'c')]),
                         {'a': [None], 'b': ['c']})
