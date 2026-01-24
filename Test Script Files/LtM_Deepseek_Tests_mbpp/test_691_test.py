import unittest
from mbpp_691_code import group_element

class TestGroupElement(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(group_element([('a', 1), ('b', 2), ('c', 1)]), {1: ['a', 'c'], 2: ['b']})

    def test_empty_input(self):
        self.assertEqual(group_element([]), {})

    def test_single_element_input(self):
        self.assertEqual(group_element([('a', 1)]), {1: ['a']})

    def test_duplicate_elements(self):
        self.assertEqual(group_element([('a', 1), ('b', 1), ('c', 2), ('d', 2)]), {1: ['a', 'b'], 2: ['c', 'd']})

    def test_negative_values(self):
        self.assertEqual(group_element([('a', -1), ('b', -2), ('c', -1)]), {-1: ['a', 'c'], -2: ['b']})

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            group_element([('a', 1), ('b', 'two'), ('c', 1)])
