import unittest
from mbpp_475_code import sort_counter

class TestSortCounter(unittest.TestCase):

    def test_typical_case(self):
        input_dict = {'a': 5, 'b': 3, 'c': 7}
        expected_output = [('c', 7), ('a', 5), ('b', 3)]
        self.assertEqual(sort_counter(input_dict), expected_output)

    def test_empty_dict(self):
        input_dict = {}
        expected_output = []
        self.assertEqual(sort_counter(input_dict), expected_output)

    def test_single_element(self):
        input_dict = {'a': 1}
        expected_output = [('a', 1)]
        self.assertEqual(sort_counter(input_dict), expected_output)

    def test_duplicate_values(self):
        input_dict = {'a': 5, 'b': 5, 'c': 3}
        expected_output = [('a', 5), ('b', 5), ('c', 3)]
        self.assertEqual(sort_counter(input_dict), expected_output)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sort_counter(123)
