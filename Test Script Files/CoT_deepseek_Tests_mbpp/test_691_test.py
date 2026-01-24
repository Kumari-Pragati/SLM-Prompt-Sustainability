import unittest
from mbpp_691_code import groupby
from 691_code import group_element

class TestGroupElement(unittest.TestCase):

    def test_typical_case(self):
        test_list = [('a', 1), ('b', 2), ('c', 2), ('d', 1), ('e', 3)]
        expected_output = {1: ['a', 'd'], 2: ['b', 'c'], 3: ['e']}
        self.assertEqual(group_element(test_list), expected_output)

    def test_empty_list(self):
        test_list = []
        expected_output = {}
        self.assertEqual(group_element(test_list), expected_output)

    def test_single_element(self):
        test_list = [('a', 1)]
        expected_output = {1: ['a']}
        self.assertEqual(group_element(test_list), expected_output)

    def test_duplicate_elements(self):
        test_list = [('a', 1), ('b', 1), ('c', 2), ('d', 2), ('e', 3), ('f', 3)]
        expected_output = {1: ['a', 'b'], 2: ['c', 'd'], 3: ['e', 'f']}
        self.assertEqual(group_element(test_list), expected_output)

    def test_invalid_input(self):
        test_list = [('a', 1), ('b', 'two'), ('c', 2), ('d', 2), ('e', 3), ('f', 3)]
        with self.assertRaises(TypeError):
            group_element(test_list)
