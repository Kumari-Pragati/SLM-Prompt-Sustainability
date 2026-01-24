import unittest
from mbpp_391_code import convert_list_dictionary

class TestConvertListDictionary(unittest.TestCase):

    def test_simple_input(self):
        l1 = [1, 2]
        l2 = ['a', 'b']
        l3 = ['x', 'y']
        expected_output = [{1: {'a': 'x'}}, {2: {'b': 'y'}}]
        self.assertEqual(convert_list_dictionary(l1, l2, l3), expected_output)

    def test_empty_input(self):
        l1 = []
        l2 = []
        l3 = []
        expected_output = []
        self.assertEqual(convert_list_dictionary(l1, l2, l3), expected_output)

    def test_boundary_conditions(self):
        l1 = [0]
        l2 = ['a']
        l3 = ['x']
        expected_output = [{0: {'a': 'x'}}]
        self.assertEqual(convert_list_dictionary(l1, l2, l3), expected_output)

    def test_complex_input(self):
        l1 = [1, 2, 3]
        l2 = ['a', 'b', 'c']
        l3 = ['x', 'y', 'z']
        expected_output = [{1: {'a': 'x'}}, {2: {'b': 'y'}}, {3: {'c': 'z'}}]
        self.assertEqual(convert_list_dictionary(l1, l2, l3), expected_output)
