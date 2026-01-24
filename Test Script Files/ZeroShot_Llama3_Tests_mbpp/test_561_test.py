import unittest
from mbpp_561_code import assign_elements

class TestAssignElements(unittest.TestCase):

    def test_assign_elements(self):
        test_list = [('a', 1), ('b', 2), ('c', 3), ('d', 1), ('e', 2)]
        expected_output = {1: ['a', 'd'], 2: ['b', 'e'], 3: ['c']}
        self.assertEqual(assign_elements(test_list), expected_output)

    def test_assign_elements_empty_list(self):
        test_list = []
        expected_output = {}
        self.assertEqual(assign_elements(test_list), expected_output)

    def test_assign_elements_single_element(self):
        test_list = [('a', 1)]
        expected_output = {1: ['a']}
        self.assertEqual(assign_elements(test_list), expected_output)

    def test_assign_elements_duplicates(self):
        test_list = [('a', 1), ('b', 2), ('c', 3), ('d', 1), ('e', 2), ('f', 3)]
        expected_output = {1: ['a', 'd'], 2: ['b', 'e'], 3: ['c', 'f']}
        self.assertEqual(assign_elements(test_list), expected_output)
