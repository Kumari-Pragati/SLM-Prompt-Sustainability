import unittest
from mbpp_691_code import groupby
from mbpp_691_code import group_element

class TestGroupElement(unittest.TestCase):

    def test_group_element(self):
        test_list = [('a', 1), ('b', 2), ('c', 1), ('d', 2), ('e', 1)]
        expected_output = {1: ['a', 'c', 'e'], 2: ['b', 'd']}
        self.assertEqual(group_element(test_list), expected_output)

    def test_group_element_empty_list(self):
        test_list = []
        expected_output = {}
        self.assertEqual(group_element(test_list), expected_output)

    def test_group_element_single_element(self):
        test_list = [('a', 1)]
        expected_output = {1: ['a']}
        self.assertEqual(group_element(test_list), expected_output)

    def test_group_element_duplicate_elements(self):
        test_list = [('a', 1), ('b', 1), ('c', 1)]
        expected_output = {1: ['a', 'b', 'c']}
        self.assertEqual(group_element(test_list), expected_output)
