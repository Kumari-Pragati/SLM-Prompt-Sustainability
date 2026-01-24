import unittest
from mbpp_512_code import count_element_freq

class TestCountElementFreq(unittest.TestCase):

    def test_typical_input(self):
        test_tuple = ((1, 2), (3, 4), (5, 6))
        expected_output = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1}
        self.assertEqual(count_element_freq(test_tuple), expected_output)

    def test_edge_case_empty_tuple(self):
        test_tuple = ()
        expected_output = {}
        self.assertEqual(count_element_freq(test_tuple), expected_output)

    def test_edge_case_single_element_tuple(self):
        test_tuple = (1,)
        expected_output = {1: 1}
        self.assertEqual(count_element_freq(test_tuple), expected_output)

    def test_edge_case_single_element_non_tuple(self):
        test_tuple = 1
        expected_output = {1: 1}
        self.assertEqual(count_element_freq(test_tuple), expected_output)

    def test_edge_case_nested_tuples(self):
        test_tuple = ((1, 2), (3, 4), (5, (6, 7)))
        expected_output = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1}
        self.assertEqual(count_element_freq(test_tuple), expected_output)

    def test_edge_case_tuple_with_duplicates(self):
        test_tuple = ((1, 2, 2), (3, 4, 4), (5, 6, 6))
        expected_output = {1: 1, 2: 2, 3: 1, 4: 2, 5: 1, 6: 2}
        self.assertEqual(count_element_freq(test_tuple), expected_output)

    def test_edge_case_tuple_with_non_hashable_elements(self):
        test_tuple = ({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6})
        with self.assertRaises(TypeError):
            count_element_freq(test_tuple)

    def test_edge_case_tuple_with_non_hashable_elements_and_duplicates(self):
        test_tuple = ({'a': 1, 'b': 2, 'b': 2}, {'c': 3, 'd': 4, 'd': 4}, {'e': 5, 'f': 6, 'f': 6})
        with self.assertRaises(TypeError):
            count_element_freq(test_tuple)
