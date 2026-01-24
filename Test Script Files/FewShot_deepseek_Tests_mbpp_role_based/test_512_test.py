import unittest
from mbpp_512_code import count_element_freq

class TestCountElementFreq(unittest.TestCase):
    def test_typical_use_case(self):
        test_tuple = (1, 2, 2, (3, 3, 3), 'a', 'a', 'b')
        expected_output = {1: 1, 2: 2, 3: 3, 'a': 2, 'b': 1}
        self.assertEqual(count_element_freq(test_tuple), expected_output)

    def test_empty_tuple(self):
        test_tuple = ()
        expected_output = {}
        self.assertEqual(count_element_freq(test_tuple), expected_output)

    def test_single_element_tuple(self):
        test_tuple = (1,)
        expected_output = {1: 1}
        self.assertEqual(count_element_freq(test_tuple), expected_output)

    def test_nested_tuple_with_same_elements(self):
        test_tuple = ((1, 2), (1, 2))
        expected_output = {1: 2, 2: 2}
        self.assertEqual(count_element_freq(test_tuple), expected_output)

    def test_nested_tuple_with_different_elements(self):
        test_tuple = ((1, 2), (3, 4))
        expected_output = {1: 1, 2: 1, 3: 1, 4: 1}
        self.assertEqual(count_element_freq(test_tuple), expected_output)

    def test_mixed_types(self):
        test_tuple = (1, 'a', [1, 2, 3], {'a': 1})
        expected_output = {1: 1, 'a': 1, [1, 2, 3]: 1, {'a': 1}: 1}
        self.assertEqual(count_element_freq(test_tuple), expected_output)
