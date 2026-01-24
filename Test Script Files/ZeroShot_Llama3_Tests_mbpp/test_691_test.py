import unittest
from mbpp_691_code import group_element

class TestGroupElement(unittest.TestCase):

    def test_group_element(self):
        test_list = [('A', 1), ('B', 1), ('C', 2), ('D', 2), ('E', 3), ('F', 3)]
        expected_result = {1: ['A', 'B'], 2: ['C', 'D'], 3: ['E', 'F']}
        self.assertEqual(group_element(test_list), expected_result)

    def test_group_element_empty_list(self):
        test_list = []
        expected_result = {}
        self.assertEqual(group_element(test_list), expected_result)

    def test_group_element_single_element(self):
        test_list = [('A', 1)]
        expected_result = {1: ['A']}
        self.assertEqual(group_element(test_list), expected_result)

    def test_group_element_multiple_elements(self):
        test_list = [('A', 1), ('B', 1), ('C', 2), ('D', 2), ('E', 3), ('F', 3), ('G', 1), ('H', 1)]
        expected_result = {1: ['A', 'B', 'G', 'H'], 2: ['C', 'D'], 3: ['E', 'F']}
        self.assertEqual(group_element(test_list), expected_result)
