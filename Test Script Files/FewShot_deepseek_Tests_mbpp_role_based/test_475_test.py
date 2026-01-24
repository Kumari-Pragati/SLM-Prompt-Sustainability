import unittest
from mbpp_475_code import sort_counter

class TestSortCounter(unittest.TestCase):
    def test_typical_use_case(self):
        input_dict = {'a': 2, 'b': 3, 'c': 1}
        expected_output = [('b', 3), ('a', 2), ('c', 1)]
        self.assertEqual(sort_counter(input_dict), expected_output)

    def test_empty_dict(self):
        input_dict = {}
        expected_output = []
        self.assertEqual(sort_counter(input_dict), expected_output)

    def test_single_element(self):
        input_dict = {'a': 1}
        expected_output = [('a', 1)]
        self.assertEqual(sort_counter(input_dict), expected_output)

    def test_same_frequency(self):
        input_dict = {'a': 2, 'b': 2, 'c': 1}
        expected_output = [('b', 2), ('a', 2), ('c', 1)]
        self.assertEqual(sort_counter(input_dict), expected_output)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sort_counter('not a dictionary')
