import unittest
from mbpp_561_code import assign_elements

class TestAssignElements(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(assign_elements([]), {})

    def test_single_element(self):
        self.assertEqual(assign_elements([('a', 1)]), {'a': [1]})

    def test_multiple_elements(self):
        self.assertEqual(assign_elements([('a', 1), ('b', 2), ('c', 1), ('d', 2)]), {'a': [1], 'b': [2], 'c': [1], 'd': [2]})

    def test_duplicate_values(self):
        self.assertEqual(assign_elements([('a', 1), ('b', 1)]), {'a': [1], 'b': [1]})

    def test_duplicate_keys(self):
        self.assertEqual(assign_elements([(1, 'a'), (1, 'b')]), {1: ['a', 'b']})
