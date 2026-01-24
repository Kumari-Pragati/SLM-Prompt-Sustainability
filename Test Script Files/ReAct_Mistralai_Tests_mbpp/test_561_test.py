import unittest
from mbpp_561_code import assign_elements

class TestAssignElements(unittest.TestCase):

    def test_empty_list(self):
        self.assertDictEqual(assign_elements([]), {})

    def test_single_element(self):
        self.assertDictEqual(assign_elements([('a', 'a'),]), {'a': ['a']})

    def test_multiple_elements(self):
        self.assertDictEqual(assign_elements([('a', 'a'), ('b', 'a'), ('c', 'b'), ('a', 'c')]), {'a': ['a', 'c'], 'b': ['c'], 'c': []})

    def test_duplicate_key_value(self):
        self.assertDictEqual(assign_elements([('a', 'a'), ('a', 'a'),]), {'a': ['a', 'a']})

    def test_duplicate_key_different_value(self):
        self.assertDictEqual(assign_elements([('a', 'a'), ('a', 'b'),]), {'a': ['a', 'b']})

    def test_duplicate_value(self):
        self.assertDictEqual(assign_elements([('a', 'a'), ('b', 'a'), ('c', 'a'),]), {'a': ['a', 'a', 'c'], 'b': [], 'c': []})

    def test_empty_key(self):
        self.assertRaises(KeyError, assign_elements, [(None, 'a'),])

    def test_empty_value(self):
        self.assertRaises(TypeError, assign_elements, [('a', None),])
